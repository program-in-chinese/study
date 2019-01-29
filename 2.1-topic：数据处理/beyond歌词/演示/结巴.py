import jieba
text="钟声响起归家的讯号"
result=jieba.cut(text)
print("切分结果:  "+",".join(result)) 
