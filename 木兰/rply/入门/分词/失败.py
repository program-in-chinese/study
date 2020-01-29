from rply import LexerGenerator

分词器母机 = LexerGenerator()

分词器母机.add('数', r'\d+')

分词器母机.add('加', r'\+')
分词器母机.add('减', r'-')

分词器 = 分词器母机.build()

for 词 in 分词器.lex('1 + 1'):
    print(词)