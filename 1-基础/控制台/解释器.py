from code import InteractiveConsole
import sys
import traceback

class ZhPyConsole(InteractiveConsole):
    """
    封装Python控制台, 对输出进行转换
    """
    字典 = {
        " is not defined": "未定义",
        "NameError": "命名错误",
        "name ": "命名"
        }

    def showtraceback(self):
        sys.last_type, sys.last_value, last_tb = ei = sys.exc_info()
        sys.last_traceback = last_tb
        try:
            行 = traceback.format_exception(ei[0], ei[1], last_tb.tb_next)
            汉化行 = []
            if sys.excepthook is sys.__excepthook__:
                for 某行 in 行:
                    for 英文 in self.字典:
                        某行 = 某行.replace(英文, self.字典[英文])
                    汉化行.append(某行)
                self.write(''.join(汉化行))
            else:
                # If someone has set sys.excepthook, we let that take precedence
                # over self.write
                sys.excepthook(ei[0], ei[1], last_tb)
        finally:
            last_tb = ei = None

def 解释器(lang=None):
    """
    zhpy解释器
    """
    控制台 = ZhPyConsole()
    控制台.interact()

if __name__=="__main__":
    解释器()