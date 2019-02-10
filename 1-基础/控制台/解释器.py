from code import InteractiveConsole
import sys
import traceback

class ZhPyConsole(InteractiveConsole):
    """
    Wrapper around Python and filter input/output to the shell
    """
    字典 = {
        " is not defined": "未定义",
        "NameError": "命名错误",
        "name ": "命名"
        }

    def push(self, line):
        self.buffer.append(line)
        source = "\n".join(self.buffer)

        more = self.runsource(source, self.filename)
        if not more:
            self.resetbuffer()
        return more

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

def interpreter(lang=None):
    """
    zhpy interpreter
    """
    try:
        import readline
    except ImportError:
        pass
    else:
        #you could change this line to bind another key instead tab.
        readline.parse_and_bind("tab: complete")
    con = ZhPyConsole()
    banner = 'zhpy in %s on top of Python %s'%(sys.platform,
                                                  sys.version.split()[0])

    # able to import modules in current directory
    sys.path.insert(0, '')
    con.interact(banner)


if __name__=="__main__":
    interpreter()