import jieba
import os

所有词 = []
词频表 = {}
词所在文件 = {}
词所在文件数 = {}
路径 = "数据"
for 文件名 in os.listdir(路径):
    print(文件名)
    with open(os.path.join(路径, 文件名)) as 文件:
        内容 = 文件.read()
        分词结果 = jieba.cut(内容)
        for 词 in 分词结果:
            if 词 != " " and len(词) != 1:
                所有词.append(词)
                if 词 in 词频表:
                    词频表[词] += 1
                    词所在文件[词].add(文件名)
                else:
                    词频表[词] = 1
                    词所在文件[词] = set([文件名])

for 词 in 词所在文件:
    词所在文件数[词] = len(词所在文件[词])

# 词频列表 = sorted(词频表.items(), key=lambda d: d[1], reverse=True)
词所在文件数列表 = sorted(词所在文件数.items(), key=lambda d: d[1], reverse=True)
print(词所在文件数列表)
