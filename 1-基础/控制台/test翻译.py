import unittest
from 解释器 import ZhPyConsole

class test功能(unittest.TestCase):

    控制台 = ZhPyConsole()
    
    def test_报错信息(self):
        self.assertEqual(self.控制台.中文化("Traceback (most recent call last):"), "回溯 (最近的调用在最后):")
        self.assertEqual(self.控制台.中文化("NameError: name '学' is not defined"), "命名错误: 命名'学'未定义")
        self.assertEqual(self.控制台.中文化("SyntaxError: invalid syntax"), "语法错误: 不正确的语法")
        self.assertEqual(self.控制台.中文化("ZeroDivisionError: division by zero"), "除零错误: 不能被0除")
        # self.assertEqual(self.控制台.中文化("NameError: free variable 'type' referenced before assignment in enclosing scope"), "命名错误: 在闭合作用域中, 自由变量'type'在引用之前未被赋值")
        # self.assertEqual(self.控制台.中文化("UnboundLocalError: local variable '学生' referenced before assignment"), "本地变量未定义错误: 本地变量'学生'在引用之前未被赋值")
        self.assertEqual(self.控制台.中文化("TypeError: must be str, not int"), "类型错误: 不能将整数自动转换为字符串")
        # self.assertEqual(self.控制台.中文化("TypeError: unsupported operand type(s) for /: 'str' and 'str'"), "类型错误: 不支持/操作数: 字符串和字符串")
        # self.assertEqual(self.控制台.中文化("TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'"),"类型错误: 不支持**或pow()的操作数: 字符串和整数"
        # self.assertEqual(self.控制台.中文化("TypeError: can't multiply sequence by non-int of type 'str'"), "类型错误: 不能用非整数的类型--字符串对序列进行累乘")
        self.assertEqual(self.控制台.中文化("AttributeError: 'list' object has no attribute 'length'"), "属性错误: 'list'个体没有属性'length'")

if __name__ == '__main__':
    unittest.main()