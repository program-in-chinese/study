import copy
import time
from random import choice, shuffle
from math import log, sqrt

#'''运行 $python main.py， 输入 y+x，y为纵坐标值，x为横坐标值。如0+2将如下落子：
#       0       1       2

#   2   _       _       _    


#   1   _       _       _    


#   0   _       _       X   

class 棋盘类(object):
    """
    棋盘 for game
    """

    def __init__(self, 宽度=8, 高度=8, 几连=5):
        self.宽度 = 宽度
        self.高度 = 高度 
        self.局面 = {} # 记录当前棋盘的状态，键是位置，值是棋子，这里用玩家来表示棋子类型
        self.几连 = 几连 # 表示几个相同的棋子连成一线算作胜利

    def init_棋盘(self):
        if self.宽度 < self.几连 or self.高度 < self.几连:
            raise Exception('棋盘宽度和高度不能小于 %d' % self.几连) # 棋盘不能过小

        self.可走 = list(range(self.宽度 * self.高度)) # 表示棋盘上所有合法的位置，这里简单的认为空的位置即合法

        for m in self.可走:
            self.局面[m] = -1 # -1表示当前位置为空

    def 走法_to_location(self, 走法):
        h = 走法  // self.宽度
        w = 走法  %  self.宽度
        return [h, w]

    def location_to_走法(self, location):
        if(len(location) != 2):
            return -1
        h = location[0]
        w = location[1]
        走法 = h * self.宽度 + w
        if(走法 not in range(self.宽度 * self.高度)):
            return -1
        return 走法

    def update(self, 玩家, 走法): # 玩家在走法处落子，更新棋盘
        self.局面[走法] = 玩家
        self.可走.remove(走法)
#'''
class MCTS(object):
    """
    AI 玩家, use Monte Carlo Tree Search with UCB
    """

    def __init__(self, 棋盘, 出手顺序, 几连=5, time=5, 最大步数=1000):

        self.棋盘 = 棋盘
        self.出手顺序 = 出手顺序 # 出手顺序
        self.计算_time = float(time) # 最大运算时间
        self.最大步数 = 最大步数 # 每次模拟对局最多进行的步数
        self.几连 = 几连

        self.玩家 = 出手顺序[0] # 轮到电脑出手，所以出手顺序中第一个总是电脑
        self.置信度 = 1.96 # UCB中的常数
        self.模拟次数 = {} # 记录着法参与模拟的次数，键形如(玩家, 走法)，即（玩家，落子）
        self.获胜次数 = {} # 记录着法获胜的次数
        self.max_depth = 1

    def get_action(self): # return 走法

        if len(self.棋盘.可走) == 1:
            return self.棋盘.可走[0] # 棋盘只剩最后一个落子位置，直接返回

        # 每次计算下一步时都要清空模拟次数和获胜次数表，因为经过AI和玩家的2步棋之后，整个棋盘的局面发生了变化，原来的记录已经不适用了——原先普通的一步现在可能是致胜的一步，如果不清空，会影响现在的结果，导致这一步可能没那么“致胜”了
        self.模拟次数 = {} 
        self.获胜次数 = {}
        simulations = 0
        begin = time.time()
        while time.time() - begin < self.计算_time:
            棋盘_copy = copy.deepcopy(self.棋盘)  # 模拟会修改棋盘的参数，所以必须进行深拷贝，与原棋盘进行隔离
            出手顺序_copy = copy.deepcopy(self.出手顺序) # 每次模拟都必须按照固定的顺序进行，所以进行深拷贝防止顺序被修改
            self.运行模拟(棋盘_copy, 出手顺序_copy) # 进行MCTS
            simulations += 1
        print("用了", time.time() - begin,'秒')
        print("总模拟=", simulations)
        走法,胜率 = self.select_one_走法() # 选择最佳着法
        location = self.棋盘.走法_to_location(走法)
        print('最大深度搜索:', self.max_depth)
        print("程序走棋: %d+%d\n" % (location[0], location[1]),'胜率百分之',胜率*100)

        return 走法

    def 运行模拟(self, 棋盘, 出手顺序):
        """
        MCTS main process
        """

        模拟次数 = self.模拟次数
        获胜次数 = self.获胜次数
        可走 = 棋盘.可走

        玩家 = self.get_玩家(出手顺序) # 获取当前出手的玩家
        visited_局面 = set() # 记录当前路径上的全部着法
        winner = -1
        扩展 = True

        # Simulation
        for t in range(1, self.最大步数 + 1):
            # Selection选择
            # 如果所有着法都有统计信息，则获取UCB最大的着法
            if all(模拟次数.get((玩家, 走法)) for 走法 in 可走):
                log_total = log(
                    sum(模拟次数[(玩家, 走法)] for 走法 in 可走))
                value, 走法 = max(
                    ((获胜次数[(玩家, 走法)] / 模拟次数[(玩家, 走法)]) +
                     sqrt(self.置信度 * log_total / 模拟次数[(玩家, 走法)]), 走法)
                    for 走法 in 可走) 
            else:
                # 否则随机选择一个着法
                走法 = choice(可走)

            棋盘.update(玩家, 走法)

            # 扩展
            # 每次模拟最多扩展一次，每次扩展只增加一个着法
            if 扩展 and (玩家, 走法) not in 模拟次数:
                扩展 = False
                模拟次数[(玩家, 走法)] = 0
                获胜次数[(玩家, 走法)] = 0
                if t > self.max_depth:
                    self.max_depth = t

            visited_局面.add((玩家, 走法))

            is_full = not len(可走)
            win, winner = self.has_a_winner(棋盘)
            if is_full or win: # 游戏结束，没有落子位置或有玩家获胜
                break

            玩家 = self.get_玩家(出手顺序)

        # Back-propagation
        for 玩家, 走法 in visited_局面:
            if (玩家, 走法) not in 模拟次数:
                continue
            模拟次数[(玩家, 走法)] += 1 # 当前路径上所有着法的模拟次数加1
            if 玩家 == winner:
                获胜次数[(玩家, 走法)] += 1 # 获胜玩家的所有着法的胜利次数加1

    def get_玩家(self, 玩家s):
        p = 玩家s.pop(0)
        玩家s.append(p)
        return p

    def select_one_走法(self):
        胜率, 走法 = max(
            (self.获胜次数.get((self.玩家, 走法), 0) /
             self.模拟次数.get((self.玩家, 走法), 1),
             走法)
            for 走法 in self.棋盘.可走) # 选择胜率最高的着法

        return 走法,胜率

    def has_a_winner(self, 棋盘):
        """
        检查是否有玩家获胜
        """
        走法d = list(set(range(棋盘.宽度 * 棋盘.高度)) - set(棋盘.可走))
        if(len(走法d) < self.几连 + 2):
            return False, -1

        宽度 = 棋盘.宽度
        高度 = 棋盘.高度
        局面 = 棋盘.局面
        n = self.几连
        for m in 走法d:
            h = m // 宽度
            w = m % 宽度
            玩家 = 局面[m]

            if (w in range(宽度 - n + 1) and
                len(set(局面[i] for i in range(m, m + n))) == 1): # 横向连成一线
                return True, 玩家

            if (h in range(高度 - n + 1) and
                len(set(局面[i] for i in range(m, m + n * 宽度, 宽度))) == 1): # 竖向连成一线
                return True, 玩家

            if (w in range(宽度 - n + 1) and h in range(高度 - n + 1) and
                len(set(局面[i] for i in range(m, m + n * (宽度 + 1), 宽度 + 1))) == 1): # 右斜向上连成一线
                return True, 玩家

            if (w in range(n - 1, 宽度) and h in range(高度 - n + 1) and
                len(set(局面[i] for i in range(m, m + n * (宽度 - 1), 宽度 - 1))) == 1): # 左斜向下连成一线
                return True, 玩家

        return False, -1

    def __str__(self):
        return "程序"
class 棋手(object):
    """
    human 玩家
    """

    def __init__(self, 棋盘, 玩家):
        self.棋盘 = 棋盘
        self.玩家 = 玩家

    def get_action(self):
        try:
            location = [int(n, 10) for n in input("你走棋（纵+横）: ").split("+")]
            走法 = self.棋盘.location_to_走法(location)
        except Exception as e:
            走法 = -1
        if 走法 == -1 or 走法 not in self.棋盘.可走:
            print("无效移动")
            走法 = self.get_action()
        return 走法

    def __str__(self):
        return "人类"
class 游戏类(object):
    """
    game server
    """

    def __init__(self, 棋盘, **kwargs):
        self.棋盘 = 棋盘
        self.玩家 = [1, 2] # 玩家1 and 玩家2
        self.几连 = int(kwargs.get('几连', 5))
        self.time = float(kwargs.get('time', 5))
        self.最大步数 = int(kwargs.get('最大步数', 10000))

    def start(self):
        p1, p2 = self.init_玩家()
        self.棋盘.init_棋盘()

        ai = MCTS(self.棋盘, [p1, p2], self.几连, self.time, self.最大步数)
        human = 棋手(self.棋盘, p2)
        玩家s = {}
        玩家s[p1] = ai
        玩家s[p2] = human
        turn = [p2, p1]
        shuffle(turn) # 玩家和电脑的出手顺序随机
        while(1):
            p = turn.pop(0)
            turn.append(p)
            玩家_in_turn = 玩家s[p]
            走法 = 玩家_in_turn.get_action()
            self.棋盘.update(p, 走法)
            self.graphic(self.棋盘, human, ai)
            end, winner = self.game_end(ai)
            if end:
                if winner != -1:
                    print("游戏结束。赢家是", 玩家s[winner])
                break

    def init_玩家(self):
        plist = list(range(len(self.玩家)))
        index1 = choice(plist)
        plist.remove(index1)
        index2 = choice(plist)

        return self.玩家[index1], self.玩家[index2]

    def game_end(self, ai):
        """
        检查游戏是否结束
        """
        win, winner = ai.has_a_winner(self.棋盘)
        if win:
            return True, winner
        elif not len(self.棋盘.可走):
            print("游戏结束。和棋")
            return True, -1
        return False, -1

    def graphic(self, 棋盘, human, ai):
        """
        在终端绘制棋盘，显示棋局的状态
        """
        宽度 = 棋盘.宽度
        高度 = 棋盘.高度

        print("人类 玩家",human.玩家, "走X".rjust(2))
        print("程序 玩家",ai.玩家, "走O".rjust(2))
        print()
        for x in range(宽度):
            print("{0:8}".format(x), end='')
        print('\r\n')
        for i in range(高度 - 1, -1, -1):
            print("{0:4d}".format(i), end='')
            for j in range(宽度):
                loc = i * 宽度 + j
                if 棋盘.局面[loc] == human.玩家:
                    print('X'.center(8), end='')
                elif 棋盘.局面[loc] == ai.玩家:
                    print('O'.center(8), end='')
                else:
                    print('_'.center(8), end='')
            print('\r\n\r\n')
def run():
    n = 3
    try:
        棋盘 = 棋盘类(宽度=3, 高度=3, 几连=n)
        game = 游戏类(棋盘, 几连=n, time=1)
        game.start()
    except KeyboardInterrupt:
        print('\n\rquit')

if __name__ == '__main__':
    run()