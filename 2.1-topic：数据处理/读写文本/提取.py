with open('三国志 copy.txt') as f:
    所有行 = f.readlines()

书名 = '吴书'

卷名 = ''
卷中行 = []
卷开始 = False
for 行 in 所有行:
    if 卷开始:
        if 行 != '\n' and 行 != '------------\n':
            卷中行.append(行.strip())
    else:
        if 卷名 == '王楼贺韦华传':
            break
        卷中行 = []

    if 行.find('｜' + 书名) > 0:
        前缀 = '、　'
        后缀 = '第'
        卷名 = 行[行.find(前缀) + 2 : 行.find(后缀)]
        卷开始 = True
        print(卷名)
    elif 行.find('------------') == 0:
        卷开始 = False
        print("转写: "+ 卷名)
        with open(书名 + '/' + 卷名 + '.js', 'w') as f1:
            f1.write('const 内容 = Object.freeze([\n')
            for 行 in 卷中行:
                f1.write("'" + 行 + "',\n")
            f1.write("])\n\nexports.内容 = 内容")
        with open(书名 + '/目录.js', 'a') as f1:
            f1.write("'" + 卷名 + "',\n")
