from PIL import Image
import os

# 参考: https://www.liaoxuefeng.com/wiki/1016959663602400/1017785454949568
原图片路径 = '/Users/xuanwu/work/机甲/2019-10-11 安装/'
目标路径 = '/Users/xuanwu/work/机甲/缩略/'
for 文件名 in os.listdir(原图片路径):
    if not 文件名.endswith('.jpg'):
        continue
    图片 = Image.open(os.path.join(原图片路径, 文件名))

    宽, 高 = 图片.size
    print('原图尺寸: %sx%s' % (宽, 高))
    
    图片.thumbnail((宽//4, 高//4))
    print('新尺寸: %sx%s' % (宽//4, 高//4))

    图片.save(目标路径 + 文件名, 'jpeg')