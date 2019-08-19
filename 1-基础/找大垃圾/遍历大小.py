import os

# 100MB
KB = 1000
兆 = 1000 * KB
GB = 1000 * 兆

阈值 = 10# * 兆

各文件大小 = {}
各路径大小 = {}

# 参考: https://stackoverflow.com/questions/1392413/calculating-a-directorys-size-using-python
def 遍历目录(起始路径 = '.'):
    总量 = 0
    for 路径, 目录名, 所有文件 in os.walk(起始路径):
        for 文件 in 所有文件:
            文件路径 = os.path.join(路径, 文件)
            # 如果是符号链接, 跳过
            if not os.path.islink(文件路径):
                文件大小 = os.path.getsize(文件路径)
                各文件大小[文件路径] = 文件大小

                if 路径 in 各路径大小:
                    各路径大小[路径] += 文件大小
                else:
                    各路径大小[路径] = 文件大小
                总量 += 文件大小

    return 总量

def sort_by_value(d): 
    items=d.items() 
    backitems=[[v[1],v[0]] for v in items] 
    backitems.sort(reverse = True)
    return backitems

def 格式化输出(字节数):
    if 字节数 > GB:
        return str(字节数 / GB) + " GB"
    elif 字节数 > 兆:
        return str(字节数 / 兆) + " MB"
    else:
        return "<1兆: " + str(字节数) + " 字节"

def 排序并输出(未排序大小表):
    已排序表 = sort_by_value(未排序大小表)
    for 文件信息 in 已排序表:
        大小 = 文件信息[0]
        if 大小 > 阈值:
            print(文件信息[1] + ": " + 格式化输出(大小))

总大小 = 遍历目录()

print("路径占空间" + 格式化输出(总大小))

排序并输出(各文件大小)
print("已排序路径信息:")
排序并输出(各路径大小)
