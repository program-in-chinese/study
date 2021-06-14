from rply import 语法分析器母机

### 分词器部分
from rply import 分词器母机

from rply.词 import BaseBox

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
        return oct(self.参数.求值())


分词母机 = 分词器母机()

分词母机.添了('数', r'\d+')
分词母机.添了('求', r'求')
分词母机.添了('的', r'的')
分词母机.添了('值', r'值')
分词母机.添了('oct', r'oct')
分词母机.略过(r'\s+')

分词器 = 分词母机.产出()

分析器母机 = 语法分析器母机(['数', '求', '的', '值', 'oct'])


@分析器母机.语法规则('函数求值 : 求 表达式 的 oct 值')
def 求值表达式(片段):
    参数 = 片段[1]
    return 函数求值(oct, 参数)


@分析器母机.语法规则('表达式 : 数')
def 数表达式(片段):
    return 数(int(片段[0].getstr()))


分析器 = 分析器母机.产出()
print(分析器.分析(分词器.分词('求8的oct值')).求值())
