from code import InteractiveConsole
import sys

class ZhPyConsole(InteractiveConsole):
    """
    Wrapper around Python and filter input/output to the shell
    """

    def push(self, line):
        self.buffer.append(line)
        source = "\n".join(self.buffer)

        more = self.runsource(source, self.filename)
        if not more:
            self.resetbuffer()
        return more

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