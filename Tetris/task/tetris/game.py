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
