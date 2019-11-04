from xml.dom import minidom

# TODO: sharp支持
对应 = {'C': "哆", 'D': "来", 'E': "咪", 'F': "发", 'G': "嗦", 'A': "啦", 'B': "西"}
#E4 D4 C3 G2 | C4 B3 A2 E2
#哆3 嗦2 
def 取子元素(节点, tag名):
    子节点 = 节点.getElementsByTagName(tag名)
    if len(子节点) == 0:
        return None
    return 子节点[0].childNodes[0].nodeValue

# MusicXML文件是网上资源, 需另行下载. 卡农简易版: https://musescore.com/user/4000051/scores/1098321
xmldoc = minidom.parse('卡农简易版.xml')
原音符列表 = xmldoc.getElementsByTagName('note')
print(len(原音符列表))
全长 = 0
全谱 = ""
音域 = {"低": 10, "高": 0}
按音阶分音符 = {}

所有音符 = []
for 音符 in 原音符列表:
    pitch节点 = 音符.getElementsByTagName('pitch')
    if len(pitch节点) == 0:
        # 休止符？
        if len(音符.getElementsByTagName('rest')) == 1:
            所有音符.append({"音": None, "音长": 取子元素(音符, 'duration'), "音阶": None})
            continue
    #print(音符.attributes['default-x'].value)
    音高 = pitch节点[0]
    音 = 取子元素(音高, 'step')
    音长 = 取子元素(音符, 'duration')
    声部 = 取子元素(音符, 'voice')
    为和弦 = (len(音符.getElementsByTagName('chord')) == 1)

    # 如有和弦, 直接略去一半(卡农专用)
    if 音长 == None or 为和弦:
        continue

    # 卡农特殊处理(只演奏一个音阶, 避免音域过宽)
    if 声部 == "5":
        continue
    音阶 = int(取子元素(音高, 'octave'))
    #print(音阶)

    音信息 = {"音": 音, "音长": 音长, "音阶": 音阶}
    所有音符.append(音信息)

    if not 音阶 in 按音阶分音符:
        按音阶分音符[音阶] = []
    按音阶分音符[音阶].append(音信息)

    if 音阶 < 音域["低"]:
        音域["低"] = 音阶
    if 音阶 > 音域["高"]:
        音域["高"] = 音阶
    全长 += int(音长)
print("长度(除歌曲长度为单位长度): " + str(全长) + ", 音域: " + str(音域))
for 音阶 in 按音阶分音符:
    print(str(音阶) + ": " + str(len(按音阶分音符[音阶])))

音域位移 = 0
if 音域["高"] - 音域["低"] > 2:
    print("音域过宽")
音域位移 = 音域["低"] - 1

# 处理休止
序号 = 1
for 音符 in 所有音符:
    if 音符["音"] == None or 音符["音阶"] > 5:
        全谱 += "None" + ", " + 音符["音长"] + ", "
    else:
        音阶 = 音符["音阶"]
        if 音阶 > 5:
            continue
        全谱 += "常量." + 对应[音符["音"]] + str(音阶 - 音域位移) + ", " + 音符["音长"] + ", "
    序号 += 1
    if 序号 % 8 == 1:
        全谱 += "\n        "
print("总个数: " + str(序号))
print(全谱)
