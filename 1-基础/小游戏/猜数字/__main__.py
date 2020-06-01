import sys, cmd, random
from ulang.runtime.env import create_globals
from ulang.parser.core import Parser

try:
    import importlib.resources as pkg_resources
except ImportError:
    # Try backported to PY<37 `importlib_resources`.
    import importlib_resources as pkg_resources

from . import ulang_sources

def main(args=None):
    源码文件 = "报名.ul"
    源码 = pkg_resources.read_text(ulang_sources, 源码文件)
    调用(源码, 源码文件)
    猜数字().cmdloop()

def 调用(源码, 文件名):
    分析器 = Parser()
    节点 = 分析器.parse(源码, 文件名)

    code = compile(节点, 文件名, 'exec')
    '''
    exec("aaa=123", globals())
    print("lev1:", aaa)
'''
    globals = create_globals(argv=[], fname=文件名)
    本地量 = {}
    exec(code, globals, 本地量)
    print("我是:", 本地量['回应'])


class 猜数字(cmd.Cmd):
    intro = "我想了个 100 之内的数，猜猜是几？"
    想的 = random.randrange(100)
    prompt = '请猜吧: '

    def default(self, 行):
        数 = int(行)
        if 数 > self.想的:
            print("太大了!")
        elif 数 < self.想的:
            print("太小了!")
        else:
            print("中了!")
            self.do_quit(行)

    def do_quit(self, arg):
        sys.exit()

if __name__ == '__main__':
    main()