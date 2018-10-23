class 坐标{
  //private  //PS: java里面，空行和空格都属于whitespace，故可以用此法，注释掉私有修饰符
  double x,y;
  public 坐标(double X,double Y){
    this.x=X; this.y=Y;
  }

  //public double 横坐标(){return this.x; } //PS：这里注释掉的代码，其实也相当于对xy值用途的说明
  //public double 纵坐标(){return this.y; }
  public void 显示坐标(){System.out.println
    ("X="+this.x+" Y="+this.y);
  }
}

class D2PD { // demo, 2 point distance

  static double 计算坐标(坐标 A, 坐标 B){//displayPoint
    double Δx = B.x - A.x;
    double Δy = B.y - A.y;
    double 距离 = Math.sqrt(Δx*Δx+Δy*Δy);
    return 距离;
  }
  static void 显示(double 结果){
    System.out.println("结果: "+结果);
  }
  public static void main(String[] args) {
    坐标 p1 = new 坐标(1,2);
    坐标 p2 = new 坐标(5,7);
    dboule 距离 = 计算坐标(p1,p2)
    显示(距离);
  }
}
