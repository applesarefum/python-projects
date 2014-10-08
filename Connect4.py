class Grid():
    row_size = 10
    col_size = 10

    def __init__(self,rows=10,cols=10,char='~'):
        self.cols = []
        for count in range(rows):
            self.cols.append(char)

class Player():
    pass

class AI(Player):
    pass

class P1(Player):
    pass

class P2(Player):
    pass

class ShellControl():
    def run(self):
        input("Welcome to Connect 4!")


if __name__ =='__main__':
    pass
    #game = ShellControl()
    #game.run()
    grid = Grid(1000,1000,'lel')
    print(grid.cols)
