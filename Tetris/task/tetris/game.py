# Write your code here
import numpy as np


class Figure:
    '''
    This class represents figures for Tetris game
    '''
    ar = [['-'] * 4] * 4
    grid = np.array(ar)

    def __init__(self, figure, grid=grid.copy()):
        self.figure = figure
        self.grid = grid
        if self.figure == 'I':
            self.grid_I = self.grid.copy()
            self.grid_first = self.grid_I.copy()
            self.grid_first[:, [1]] = 0
            self.grid_second = self.grid_first.copy()
            self.grid_second = self.grid_second.transpose()
            self.grid_third = self.grid_first
            self.grid_fourth = self.grid_second
            self.moves = [self.grid_first, self.grid_second, self.grid_third, self.grid_fourth, self.grid_first]
        elif self.figure == 'S':
            self.grid_S = self.grid.copy()
            self.grid_first = self.grid_S.copy()
            self.grid_first[2, [0, 1]] = 0
            self.grid_first[1, [1, 2]] = 0
            self.grid_second = self.grid_first
            self.grid_second = self.grid_second.transpose()
            self.grid_third = self.grid_first
            self.grid_fourth = self.grid_second
            self.moves = [self.grid_first, self.grid_second, self.grid_third, self.grid_fourth, self.grid_first]
        elif self.figure == 'Z':
            self.grid_z = self.grid.copy()
            self.grid_first = self.grid_z.copy()
            self.grid_first[2, [1, 2]] = 0
            self.grid_first[1, [0, 1]] = 0
            self.grid_second = self.grid_z.copy()
            self.grid_second[0:2, 2] = 0
            self.grid_second[1:3, 1] = 0
            self.grid_third = self.grid_first
            self.grid_fourth = self.grid_second
            self.moves = [self.grid_first, self.grid_second, self.grid_third, self.grid_fourth, self.grid_first]
        elif self.figure == 'L':
            self.grid_L = self.grid.copy()
            self.grid_first = self.grid_L.copy()
            self.grid_first[0:3, 2] = 0
            self.grid_first[2, 1] = 0
            self.grid_second = self.grid_L.copy()
            self.grid_second[1, 0:3] = 0
            self.grid_second[2, 2] = 0
            self.grid_third = self.grid_L.copy()
            self.grid_third[0:3, 1] = 0
            self.grid_third[0, 2] = 0
            self.grid_fourth = self.grid_L.copy()
            self.grid_fourth[0, 0:3] = 0
            self.grid_fourth[1, 0] = 0
            self.moves = [self.grid_first, self.grid_second, self.grid_third, self.grid_fourth, self.grid_fourth]
        elif self.figure == 'J':
            self.grid_J = self.grid.copy()

            self.grid_first = self.grid_J.copy()
            self.grid_first[0:3, 2] = 0
            self.grid_first[2, 1] = 0

            self.grid_second = self.grid_J.copy()
            self.grid_second[1, 0:3] = 0
            self.grid_second[2, 2] = 0

            self.grid_third = self.grid_J.copy()
            self.grid_third[0:3, 1] = 0
            self.grid_third[0, 2] = 0

            self.grid_fourth = self.grid_J.copy()
            self.grid_fourth[1, 0:3] = 0
            self.grid_fourth[0, 0] = 0
            self.moves = [self.grid_first, self.grid_second, self.grid_third, self.grid_fourth, self.grid_first]
        elif self.figure == 'O':
            self.grid_O = self.grid.copy()
            self.grid_O[1:3, 1:3] = 0

            self.moves = [self.grid_O, self.grid_O, self.grid_O, self.grid_O, self.grid_O]
        elif self.figure == 'T':
            self.grid_T = self.grid.copy()
            self.grid_first = self.grid_T.copy()
            self.grid_first[1, 0:3] = 0
            self.grid_first[0, 1] = 0

            self.grid_second = self.grid_T.copy()
            self.grid_second[0:3, 1] = 0
            self.grid_second[1, 0] = 0

            self.grid_third = self.grid_T.copy()
            self.grid_third[1, 0:3] = 0
            self.grid_third[2, 1] = 0

            self.grid_fourth = self.grid_T.copy()
            self.grid_fourth[0:3, 1] = 0
            self.grid_fourth[1, 2] = 0
            self.moves = [self.grid_first, self.grid_second, self.grid_third, self.grid_fourth, self.grid_first]

    def show(self):
        for j in self.grid:
            print(' '.join(map(str, j)))
        print()
        for i in self.moves:
            for j in i:
                print(' '.join(map(str, j)))
            print()


i_fig = Figure('I')
s_fig = Figure('S')
z_fig = Figure('Z')
l_fig = Figure('L')
j_fig = Figure('J')
o_fig = Figure('O')
t_fig = Figure('T')

command = input()
if command == 'T':
    t_fig.show()
elif command == 'I':
    i_fig.show()
elif command == 'S':
    s_fig.show()
elif command == 'Z':
    z_fig.show()
elif command == 'L':
    l_fig.show()
elif command == 'J':
    j_fig.show()
elif command == 'O':
    o_fig.show()
