# Write your code here
'''import numpy as np
SIZE1 = 4
SIZE2 = 4

class Figure:
    '''
#This class represents figures for Tetris game
'''
    ar = [['-'] * SIZE1] * SIZE2
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
'''
import numpy as np


class Model:
    #MODEL_SHAPE_SIZE_X = 10
    #MODEL_SHAPE_SIZE_Y = 20
    all_models = {
        'O': [[4, 14, 15, 5], [4, 14, 15, 5], [4, 14, 15, 5], [4, 14, 15, 5]],
        'I': [[4, 14, 24, 34], [3, 4, 5, 6], [4, 14, 24, 34], [3, 4, 5, 6]],
        'S': [[5, 4, 14, 13], [4, 14, 15, 25], [5, 4, 14, 13], [4, 14, 15, 25]],
        'Z': [[4, 5, 15, 16], [5, 15, 14, 24], [4, 5, 15, 16], [5, 15, 14, 24]],
        'L': [[4, 14, 24, 25], [5, 15, 14, 13], [4, 5, 15, 25], [6, 5, 4, 14]],
        'J': [[5, 15, 25, 24], [15, 5, 4, 3], [5, 4, 14, 24], [4, 14, 15, 16]],
        'T': [[4, 14, 24, 15], [4, 13, 14, 15], [5, 15, 25, 14], [4, 5, 6, 15]]
    }

    def __init__(self, type_model='O',MODEL_SHAPE_SIZE_X=10, MODEL_SHAPE_SIZE_Y=20 ):
        self.MODEL_SHAPE_SIZE_X = MODEL_SHAPE_SIZE_X
        self.MODEL_SHAPE_SIZE_Y = MODEL_SHAPE_SIZE_Y
        self.field = np.array([['-'] * self.MODEL_SHAPE_SIZE_X] * self.MODEL_SHAPE_SIZE_Y)
        self.model = self.field.copy()

        self.positions = np.array(Model.all_models[type_model].copy())
        self.saved_positions = [[], [], [], []]
        self.current_positions = 0
        for model_position in range(len(self.positions)):
            for coordinate in self.positions[model_position]:
                row_coordinate = coordinate // self.MODEL_SHAPE_SIZE_X
                column_coordinate = coordinate % self.MODEL_SHAPE_SIZE_X
                self.model[row_coordinate][column_coordinate] = 0
            self.saved_positions[model_position] = self.model
            self.model = self.field.copy()

    def draw(self):
        if '0' in self.saved_positions[self.current_positions][-1]:
            return
        for model_position in range(len(self.positions)):
            for coordinate in self.positions[model_position]:
                row_coordinate = coordinate // self.MODEL_SHAPE_SIZE_X
                column_coordinate = coordinate % self.MODEL_SHAPE_SIZE_X
                if row_coordinate < self.MODEL_SHAPE_SIZE_Y and column_coordinate < self.MODEL_SHAPE_SIZE_X:
                    self.model[row_coordinate][column_coordinate] = 0
                else:
                    if row_coordinate >= self.MODEL_SHAPE_SIZE_Y and column_coordinate < self.MODEL_SHAPE_SIZE_X:
                        self.model[self.MODEL_SHAPE_SIZE_Y - 1][self.MODEL_SHAPE_SIZE_X - 1] = 0
                    elif row_coordinate >= self.MODEL_SHAPE_SIZE_Y:
                        self.model[self.MODEL_SHAPE_SIZE_Y - 1][column_coordinate] = 0
                    elif column_coordinate >= self.MODEL_SHAPE_SIZE_X:
                        self.model[row_coordinate][self.MODEL_SHAPE_SIZE_X - 1] = 0



            self.saved_positions[model_position] = self.model
            self.model = self.field.copy()
        #    self.current_positions = self.saved_positions[0]

    def move_down(self):
        if '0' not in self.saved_positions[self.current_positions][-1]:
            for i in self.positions:
                i += 10
            Model.draw(self)
        Model.print_out(self)

    def move_right(self):
        if '0' not in self.saved_positions[self.current_positions][:, -1]:
            for i in self.positions:
                for j in range(len(i)):
                    if i[j] % 10 == 9:
                        i[j] -= 9
                    else:
                        i[j] += 1
        Model.move_down(self)
      #  print(self.positions[0])

    def move_left(self):
        if '0' not in self.saved_positions[self.current_positions][:, 0]:
            for i in self.positions:
                for j in range(len(i)):
                    if i[j] % 10 == 0:
                        i[j] += 9
                    else:
                        i[j] -= 1
           # print(self.positions[0])
        Model.move_down(self)

    def rotate(self):
        if '0' not in self.saved_positions[self.current_positions][:, -1]:
            if self.current_positions < 3:
                self.current_positions += 1
            else:
                self.current_positions = 0
            Model.move_down(self)
        else:
            Model.print_out(self)

    def print_out(self):
        for i in self.saved_positions[self.current_positions]:
          #  for j in i:
            print(' '.join(map(str, i)))
       # print()




type_of_model = input().split()
dimensions = input().split()

obj_model = Model(type_model=type_of_model[0], MODEL_SHAPE_SIZE_X=int(dimensions[0]), MODEL_SHAPE_SIZE_Y=int(dimensions[1]))

print()
for i in obj_model.model:
    print(' '.join(map(str, i)))
print()
obj_model.print_out()
while True:
    cmd = input()
    print()
    if cmd == 'exit':
        break
    elif cmd == 'rotate':
        obj_model.rotate()
    elif cmd == 'left':
        obj_model.move_left()
    elif cmd == 'right':
        obj_model.move_right()
    elif cmd == 'down':
        obj_model.move_down()
