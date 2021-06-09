from rply import ParserGenerator

### 分词器部分
from rply import LexerGenerator

分词器母机 = LexerGenerator()

分词器母机.add('数', r'\d+')
分词器母机.add('求', r'求')
分词器母机.add('的', r'的')
分词器母机.add('值', r'值')
分词器母机.add('oct', r'oct')

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
     'oct',
    ],
)

# 如此规则不置于前，报警 ParserGeneratorWarning: Production '函数求值' is not reachable 且解析出错，详见：
# https://github.com/alex/rply/issues/108#issuecomment-857163639
@分析器母机.production('函数求值 : 求 表达式 的 oct 值')
def 求值表达式(片段):
    参数 = 片段[1]
    return 函数求值(oct, 参数)

@分析器母机.production('表达式 : 数')
def 数表达式(片段):
    # 匹配规则右部的片段列表
    return 数(int(片段[0].getstr()))

分析器 = 分析器母机.build()

for 词 in 分词器.lex('求8的oct值'):
    print(词)

print(分析器.parse(分词器.lex('求8的oct值')).求值())