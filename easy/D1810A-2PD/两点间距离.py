class 坐标:
    def __init__(此,横,纵):
        此.x, 此.y = 横,纵

    def __repr__(此):  # 显示坐标; 例： print 坐标(1,1)
        print(
            "X="+此.x+" Y="+此.y)

def 计算(A:坐标,B:坐标):  # 这里用了py3.5+的type hint
    开方 = __import__('math').sqrt
    Δx = B.x - A.x
    Δy = B.y - A.y
    距离 = 开方(Δx**2+Δy**2)
    return 距离

def 解():
    结果 = 计算(坐标(1,2),坐标(5,7))
    print(结果)

if __name__ == '__main__':
    解()
