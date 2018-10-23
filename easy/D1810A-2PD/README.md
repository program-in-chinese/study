> 2PD=2PointDistance

题：计算平面坐标内，(1,2)到(5,7)的距离

原题：用java实现Point类，并实现displayPoint()方法/用以显示该点坐标；要求计算出(1,2)到(5,7)的距离

备注：这里先规定距离是标量/不带方向

在线测试：https://repl.it/@s6dyl/Debug1021?language=java

APL: https://tryapl.org/?a=(((5-1)*2)+(7-2)*2)*0.5&run

Kdb+/q：
```q
{sqrt ((y[0]-x[0])xexp 2)+(y[1]-x[1])xexp 2}[(1;2);(5;7)]
```
