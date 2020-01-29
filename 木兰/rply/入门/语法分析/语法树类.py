from rply.token import BaseBox

class 数(BaseBox):
    def __init__(self, 值):
        self.值 = 值

    def 求值(self):
        return self.值

class 二元运算符(BaseBox):
    def __init__(self, 左, 右):
        self.左 = 左
        self.右 = 右

class 加(二元运算符):
    def 求值(self):
        return self.左.求值() + self.右.求值()

class 减(二元运算符):
    def 求值(self):
        return self.左.求值() - self.右.求值()

class 乘(二元运算符):
    def 求值(self):
        return self.左.求值() * self.右.求值()

class 除(二元运算符):
    def 求值(self):
        return self.左.求值() / self.右.求值()