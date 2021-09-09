# pip install rply-ulang==0.7.10 可运行

from rply import ParserGenerator

### 分词器部分
from rply import LexerGenerator

分词器母机 = LexerGenerator()

分词器母机.add('数', r'\d+')
分词器母机.add('求', r'求')
分词器母机.add('的', r'的')
分词器母机.add('值', r'值')
分词器母机.add('标识符', r'\$?[_a-zA-Z][_a-zA-Z0-9]*')


分词器母机.ignore(r'\s+')

分词器 = 分词器母机.build()

### 语法树部分

from rply.token import BaseBox

class 数(BaseBox):
    def __init__(self, 值):
        self.值 = 值

    def 求值(self):
        return self.值


class 函数求值(BaseBox):
    def __init__(self, 函数, 参数):
        self.函数 = 函数
        self.参数 = 参数

    def 求值(self):
        return oct(self.参数.求值()) #self.函数


### 语法分析器部分

分析器母机 = ParserGenerator(
    # 所有词名
    ['数',
     '求',
     '的',
     '值',
     '标识符',
    ],
)

@分析器母机.production('表达式 : 数')
def 数表达式(片段):
    # 匹配规则右部的片段列表
    return 数(int(片段[0].getstr()))

# 语法分析/函数.py:61: ParserGeneratorWarning: Production '函数求值' is not reachable
@分析器母机.production('表达式 : 求 表达式 的 标识符 值')
def 求值表达式(片段):
    参数 = 片段[1]
    函数 = 片段[-2].getstr()
    return 函数求值(oct, 参数)

分析器 = 分析器母机.build()

for 词 in 分词器.lex('求求8的oct值的abs值'):
    print(词)

print(分析器.parse(分词器.lex('求8的oct值')).求值())