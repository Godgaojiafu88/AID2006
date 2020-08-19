map = [
    [2, 0, 0, 2],
    [4, 2, 0, 2],
    [2, 4, 2, 4],
    [0, 4, 0, 4],
]
list_merge=[]

class Game2048Viem:
    def __init__(self):
        self.controller=Game2048Controller()

    def __display_menu(self):
        for i in range(len(map)):
            print(map[i])



    def print_direction(self):
        direction=input("请输入方向(上下左右)")
        if direction=="左":
            self.controller.move_left()
        elif direction=="右":
            self.controller.move_right()
        elif direction=="上":
            self.controller.move_up()
        elif direction=="下":
            self.controller.move_down()
    def main(self):
        while True:
            self.__display_menu()
            self.print_direction()




class Game2048Controller:
    def zero_to_end(self):#零元素后移
        for i in range(len(list_merge) - 1, -1, -1):
            if list_merge[i] == 0:
                del list_merge[i]
                list_merge.append(0)

    def merge(self):#合并
        self.zero_to_end()
        for i in range(len(list_merge) - 1):
            if list_merge[i] == list_merge[i + 1]:
                list_merge[i] += list_merge[i + 1]
                del list_merge[i + 1]
                list_merge.append(0)

    def move_left(self):#向左
        global list_merge
        for line in map:
            list_merge = line
            self.merge()


    def move_right(self):#向右
        global list_merge
        for line in map:
            list_merge = line[::-1]
            self.merge()
            line[::-1] = list_merge

    def square_matrix_transposition(self):#转置
        for c in range(1, len(map)):  # 1 2 3
            for r in range(c, len(map)):
                map[r][c - 1], map[c - 1][r] = map[c - 1][r], map[r][c - 1]

    def move_up(self):#向上
        self.square_matrix_transposition()
        self.move_left()
        self.square_matrix_transposition()

    def move_down(self):#向下
        self.square_matrix_transposition()
        self.move_right()
        self.square_matrix_transposition()
view=Game2048Viem()
view.main()