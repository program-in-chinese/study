import json
import re
from pprint import pprint

# 源自 https://stackoverflow.com/a/29920015/1536803
def camel_case_split(identifier):
    matches = re.finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', identifier)
    return [m.group(0) for m in matches]

with open('CTS_字典_dictconfig.json') as 字典文件:
    原始字典 = json.load(字典文件)

初始字典 = 原始字典['汉英多译']
总词条数 = len(初始字典)
新提取词条数 = 0

翻译表 = 原始字典['通用词典']

for 英文 in 翻译表:
    前部分有翻译 = False
    拆分词 = camel_case_split(英文)
    翻译 = 翻译表[英文]
    前部分翻译 = ''
    for 索引 in range(0, len(拆分词)):
        词 = 拆分词[索引]
        小写词 = 词.lower()
        if 小写词 in 初始字典:
            if 翻译.find(前部分翻译 + 初始字典[小写词]) == 0:
                前部分翻译 += 初始字典[小写词]
                前部分有翻译 = True
                pass
            else:
                # print("'" + 翻译 + "'与字典有出入: " + 初始字典[小写词] + " <-> " + 翻译)
                continue
        else:
            # 如仅有一词, 直接作为新词条
            if len(拆分词) == 1:
                # 新提取词条数 += 1
                # print("从'" + 翻译 + "'提取词条: " + 小写词 + " -> " + 翻译)
                pass
            # 如词组中仅有一词不在术语词典, 那么将此词和剩余翻译提取为词条
            # 比如: "timestampOffset": "时间戳偏移", 词典中已有timestamp->时间戳, 那么剩下的词offset可提取为新词条, 释义为"偏移"
            elif 前部分有翻译 and 索引 > 0 and 索引 == len(拆分词) - 1:
                新提取词条数 += 1
                # print(前部分翻译)
                print("从'" + 翻译 + "'提取词条: " + 小写词 + " -> " + 翻译[len(前部分翻译):])
            else:
                continue

print("新提取词条数: " + str(新提取词条数))