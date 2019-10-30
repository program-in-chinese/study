# 源自：https://blog.csdn.net/hitzijiyingcai/article/details/81152174
词语 = '用中文编程'
所有行 = []
for 行数 in range(30, -30, -1):
    一行 = []
    for 列数 in range(-30,30):
        x某 = 列数 * 0.05
        y某 = 行数 * 0.05
        字 = ""
        if (x某 ** 2 + y某 ** 2 - 1 ) ** 3 - x某 ** 2 * y某 ** 3 <= 0:
            字 = 词语[(列数 - 行数) % len(词语)]
        else:
            字 = '一'
        一行.append(字)
    所有行.append(''.join(一行))
print('\n'.join(所有行))