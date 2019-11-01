from xml.dom import minidom

对应 = {'C': "哆", 'D': "来", 'E': "咪", 'F': "发", 'G': "嗦", 'A': "啦", 'B': "西"}

def 取子元素(节点, tag名):
    return 节点.getElementsByTagName(tag名)[0].childNodes[0].nodeValue

# MusicXML文件是网上资源, 需另行下载
xmldoc = minidom.parse('彩云追月.xml')
原音符列表 = xmldoc.getElementsByTagName('note')
print(len(原音符列表))
全长 = 0
全谱 = ""
音域 = {"低": 10, "高": 0}

所有音符 = []
for 音符 in 原音符列表:
    音高 = 音符.getElementsByTagName('pitch')[0]
    音 = 取子元素(音高, 'step')
    音长 = 取子元素(音符, 'duration')
    音阶 = int(取子元素(音高, 'octave'))

    所有音符.append({"音": 音, "音长": 音长, "音阶": 音阶})

    if 音阶 < 音域["低"]:
        音域["低"] = 音阶
    if 音阶 > 音域["高"]:
        音域["高"] = 音阶
    全长 += int(音长)
print("长度: " + str(全长) + ", 音域: " + str(音域))

音域位移 = 0
if 音域["高"] - 音域["低"] > 2:
    print("音域过宽")
else:
    音域位移 = 音域["低"] - 1

for 音符 in 所有音符:
    全谱 += "常量." + 对应[音符["音"]] + str(音符["音阶"] - 音域位移) + ", " + 音符["音长"] + ", "

print(全谱)
