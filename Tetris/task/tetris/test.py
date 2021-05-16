import numpy as np


class Model:
    MODEL_SHAPE_SIZE_X = 10
    MODEL_SHAPE_SIZE_Y = 20
    all_models = {
        'O': [[4, 14, 15, 5], [4, 14, 15, 5], [4, 14, 15, 5], [4, 14, 15, 5]],
        'I': [[4, 14, 24, 34], [3, 4, 5, 6], [4, 14, 24, 34], [3, 4, 5, 6]],
        'S': [[5, 4, 14, 13], [4, 14, 15, 25], [5, 4, 14, 13], [4, 14, 15, 25]],
        'Z': [[4, 5, 15, 16], [5, 15, 14, 24], [4, 5, 15, 16], [5, 15, 14, 24]],
        'L': [[4, 14, 24, 25], [5, 15, 14, 13], [4, 5, 15, 25], [6, 5, 4, 14]],
        'J': [[5, 15, 25, 24], [15, 5, 4, 3], [5, 4, 14, 24], [4, 14, 15, 16]],
        'T': [[4, 14, 24, 15], [4, 13, 14, 15], [5, 15, 25, 14], [4, 5, 6, 15]]
    }

    def draw(self):
        '''        for model_position in self.positions:
            for coordinate in model_position:
                row_coordinate = coordinate // Model.MODEL_SHAPE_SIZE_X  # изменить на константу
                column_coordinate = coordinate % Model.MODEL_SHAPE_SIZE_X  # изменить на константу
                self.model[row_coordinate][column_coordinate] = 0
            self.saved_positions.append(self.model)
            self.model = self.field.copy()'''
        for model_position in range(len(self.positions)):
            for coordinate in self.positions[model_position]:
                row_coordinate = coordinate // Model.MODEL_SHAPE_SIZE_X  # изменить на константу
                column_coordinate = coordinate % Model.MODEL_SHAPE_SIZE_X  # изменить на константу
                self.model[row_coordinate][column_coordinate] = 0
            self.saved_positions[model_position] = self.model
            self.model = self.field.copy()


    def __init__(self, type_model='O'):
        self.field = np.array([['-'] * Model.MODEL_SHAPE_SIZE_X] * Model.MODEL_SHAPE_SIZE_Y)
        self.model = self.field.copy()
        self.positions = np.array(Model.all_models[type_model].copy())
        self.saved_positions = [[], [], [], []]
        '''        for model_position in self.positions:
            for coordinate in model_position:
                row_coordinate = coordinate // Model.MODEL_SHAPE_SIZE_X  
                column_coordinate = coordinate % Model.MODEL_SHAPE_SIZE_X 
                self.model[row_coordinate][column_coordinate] = 0
            self.saved_positions.append(self.model)
            self.model = self.field.copy()'''

        for model_position in range(len(self.positions)):
            for coordinate in self.positions[model_position]:
                row_coordinate = coordinate // Model.MODEL_SHAPE_SIZE_X
                column_coordinate = coordinate % Model.MODEL_SHAPE_SIZE_X
                self.model[row_coordinate][column_coordinate] = 0
            self.saved_positions[model_position] = self.model
            self.model = self.field.copy()

    def move_down(self):
        for i in self.positions:
            i += 10
    def move_right(self):
        for i in self.positions:
            i += 11

        for i in self.positions:
            if i.any() % 10 == 1:
                i -= 10
    def move_left(self):
        for i in self.positions:
            for j in i:
                print(j)
                j += 9
                print(j)
        for i in self.positions:
            for j in i:
                if j % 10 == 0:
                    print('here')
                    print(i)
                    j -= 40
        print(self.positions)






a = Model('O')
a.move_left()
a.move_left()
a.move_left()
a.move_left()
a.move_left()


a.draw()
print(a.saved_positions[0])

a = np.array([i for i in range(5)])
print(a)
for i in a:
    if i > 0:
        i += 1
print(a)
