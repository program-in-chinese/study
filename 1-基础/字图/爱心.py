# 源自：https://blog.csdn.net/hitzijiyingcai/article/details/81152174
词语 = '用中文编程'
所有行 = []
for 行数 in range(15, -15, -1):
    一行 = []
    for 列数 in range(-15,15):
        列 = 列数 * 0.12
        行 = 行数 * 0.12
        字 = ""
        if (列 ** 2 + 行 ** 2 - 1) ** 3 <= 列 ** 2 * 行 ** 3:
            字 = 词语[(列数 - 行数) % len(词语)]
        else:
            字 = '一'
        一行.append(字)
    所有行.append(''.join(一行))
print('\n'.join(所有行))