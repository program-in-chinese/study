# 源自：https://blog.csdn.net/hitzijiyingcai/article/details/81152174
词语 = '中文编程'
所有行 = []
for 行 in range(15,-15,-1):
    所有字段 = []
    for x in range(-15,15):
        x某 = x * 0.1
        y某 = 行 * 0.1
        所有字段.append(词语[(x - 行) % len(词语)] if (x某 ** 2 + y某 ** 2 - 1 ) ** 3 - x某 ** 2 * y某 ** 3 <= 0 else '一')
    所有行.append(''.join(所有字段))
print('\n'.join(所有行))