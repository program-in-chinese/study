# Python 3.7.3下测试通过
# 参考: https://stackoverflow.com/a/48817000/1536803
import sys
from xml.etree import ElementTree as 结构

根 = 结构.Element('html')
body = 结构.Element('body')
根.append(body)
div = 结构.Element('div')
body.append(div)
span = 结构.Element('span')
div.append(span)
span.text = "待文本生成"

结构.ElementTree(根).write('测1.html', encoding='unicode', method='html')