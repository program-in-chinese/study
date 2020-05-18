import sys, cmd, random

def main(args=None):
    猜数字().cmdloop()

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