from code import InteractiveConsole
import re
import sys
import traceback

class ZhPyConsole(InteractiveConsole):
    """
    封装Python控制台, 对输出进行转换
    """
    字典 = {
        "Traceback (most recent call last):": "回溯 (最近的调用在最后):",
        "SyntaxError: invalid syntax": "语法错误: 不正确的语法",
        "ZeroDivisionError: division by zero": "除零错误: 不能被0除",
        "TypeError: must be str, not int": "类型错误: 不能将整数自动转换为字符串"
        }

    def showtraceback(self):
        sys.last_type, sys.last_value, 回溯信息 = 运行信息 = sys.exc_info()
        sys.last_traceback = 回溯信息
        try:
            行 = traceback.format_exception(运行信息[0], 运行信息[1], 回溯信息.tb_next)
            汉化行 = []
            if sys.excepthook is sys.__excepthook__:
                for 某行 in 行:
                    汉化行.append(self.中文化(某行))
                self.write(''.join(汉化行))
            else:
                # If someone has set sys.excepthook, we let that take precedence
                # over self.write
                sys.excepthook(运行信息[0], 运行信息[1], 回溯信息)
        finally:
            回溯信息 = 运行信息 = None

    def 中文化(self, 原始信息):
        if 原始信息 in self.字典:
            return self.字典[原始信息]
        return self.模式替换(原始信息)

    # 参考: https://docs.python.org/3/library/re.html#re.sub
    def 模式替换(self, 原始信息):
        if re.match(r"NameError: name '(.*)' is not defined", 原始信息):
            return re.sub(r"NameError: name '(.*)' is not defined", r"命名错误: 命名'\1'未定义", 原始信息)
        elif re.match(r"AttributeError: '(.*)' object has no attribute '(.*)'", 原始信息):
            return re.sub(r"AttributeError: '(.*)' object has no attribute '(.*)'", r"属性错误: '\1'个体没有'\2'属性", 原始信息)
        elif re.match(r"NameError: free variable '(.*)' referenced before assignment in enclosing scope", 原始信息):
            return re.sub(r"NameError: free variable '(.*)' referenced before assignment in enclosing scope", r"命名错误: 在闭合作用域中, 自由变量'\1'在引用之前未被赋值", 原始信息)
        elif re.match(r"UnboundLocalError: local variable '(.*)' referenced before assignment", 原始信息):
            return re.sub(r"UnboundLocalError: local variable '(.*)' referenced before assignment", r"本地变量未定义错误: 本地变量'\1'在引用之前未被赋值", 原始信息)
        elif re.match(r"TypeError: unsupported operand type\(s\) for /: '(.*)' and '(.*)'", 原始信息):
            return re.sub(r"TypeError: unsupported operand type\(s\) for /: '(.*)' and '(.*)'", r"类型错误: 不支持/的操作数: '\1'和'\2'", 原始信息)
        elif re.match(r"TypeError: unsupported operand type\(s\) for \*\* or pow\(\): '(.*)' and '(.*)'", 原始信息):
            return re.sub(r"TypeError: unsupported operand type\(s\) for \*\* or pow\(\): '(.*)' and '(.*)'", r"类型错误: 不支持**或pow()的操作数: '\1'和'\2'", 原始信息)
        elif re.match(r"TypeError: can't multiply sequence by non-int of type '(.*)'", 原始信息):
            return re.sub(r"TypeError: can't multiply sequence by non-int of type '(.*)'", r"类型错误: 不能用非整数的类型--'\1'对序列进行累乘", 原始信息)
        else:
            return 原始信息

def 解释器(lang=None):
    """
    zhpy解释器
    """
    控制台 = ZhPyConsole()
    控制台.interact()

if __name__=="__main__":
    解释器()