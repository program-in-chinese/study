import os
import re

字次数 = {}
with open("红楼梦_.txt") as 文件:
    内容 = 文件.read()
    # print(内容)
    for 字 in 内容:
        if 字 in 字次数:
            字次数[字] += 1
        else:
            字次数[字] = 1

字数 = 0
for 字 in 字次数:
    if re.search(u'[\u4e00-\u9fff]', 字) == None:
        # 注: 文本文档中有不少错字, 比如一些日文字符:ぴばの. 加上特殊字符, 数字, 284 个
        # print(字)
        pass
    else:
        字数 += 1

# 汉字单字 4253 个, 算上上面的错字, 最多不超过 4537 个单字
print("单字数: " + str(字数))