from code import InteractiveConsole
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
        "TypeError: must be str, not int": "类型错误: 不能将整数自动转换为字符串",
        "AttributeError": "属性错误",
        " object has no attribute ": "个体没有属性",
        " is not defined": "未定义",
        "NameError": "命名错误",
        "name ": "命名"
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
        for 英文 in self.字典:
            原始信息 = 原始信息.replace(英文, self.字典[英文])
        return 原始信息

def 解释器(lang=None):
    """
    zhpy解释器
    """
    控制台 = ZhPyConsole()
    控制台.interact()

if __name__=="__main__":
    解释器()