import os

路径 = "../数据"
for 文件名 in os.listdir(路径):
  print(文件名)
  with open(os.path.join(路径, 文件名)) as myfile:
    内容 = myfile.read()
    print(内容)