from ulang.runtime.env import create_globals
from ulang.parser.core import Parser

# 包内嵌木兰源码文件(作为资源文件), 参考:
# https://stackoverflow.com/questions/6028000/how-to-read-a-static-file-from-inside-a-python-package
# https://stackoverflow.com/questions/11848030/how-include-static-files-to-setuptools-python-package/11848281#11848281

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

def 调用(源码, 文件名):
    分析器 = Parser()
    节点 = 分析器.parse(源码, 文件名)

    code = compile(节点, 文件名, 'exec')

    globals = create_globals(argv=[], fname=文件名)

    # 传出变量, 参考:
    # https://stackoverflow.com/questions/45535284/exec-and-variable-scope
    # https://stackoverflow.com/questions/1463306/how-does-exec-work-with-locals
    # https://docs.python.org/3/library/functions.html#exec
    本地量 = {}
    exec(code, globals, 本地量)
    # print("我是:", 本地量['回应'])

if __name__ == '__main__':
    main()