import imageio

图片 = []
for 序号 in range(0, 11):
    图片.append(imageio.imread("螺旋_" + str(序号) + ".png"))
输出文件 = '螺旋.gif'
imageio.mimsave(输出文件, 图片, duration = 0.045)