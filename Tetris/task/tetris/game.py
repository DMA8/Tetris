import numpy as np


class Model:
    # координаты всех моделей
    storage_freezed = set()
    all_models = {
        'O': [[4, 14, 15, 5], [4, 14, 15, 5], [4, 14, 15, 5], [4, 14, 15, 5]],
        'I': [[4, 14, 24, 34], [3, 4, 5, 6], [4, 14, 24, 34], [3, 4, 5, 6]],
        'S': [[5, 4, 14, 13], [4, 14, 15, 25], [5, 4, 14, 13], [4, 14, 15, 25]],
        'Z': [[4, 5, 15, 16], [5, 15, 14, 24], [4, 5, 15, 16], [5, 15, 14, 24]],
        'L': [[4, 14, 24, 25], [5, 15, 14, 13], [4, 5, 15, 25], [6, 5, 4, 14]],
        'J': [[5, 15, 25, 24], [15, 5, 4, 3], [5, 4, 14, 24], [4, 14, 15, 16]],
        'T': [[4, 14, 24, 15], [4, 13, 14, 15], [5, 15, 25, 14], [4, 5, 6, 15]]
    }

    def __init__(self, type_model='O', MODEL_SHAPE_SIZE_X=10, MODEL_SHAPE_SIZE_Y=20, field=None):
        self.MODEL_SHAPE_SIZE_X = MODEL_SHAPE_SIZE_X  # ширина поля игрового
        self.MODEL_SHAPE_SIZE_Y = MODEL_SHAPE_SIZE_Y  # высота поля игрового
        print('field is ',field)
        if field is None:
            self.field = np.array([['-'] * self.MODEL_SHAPE_SIZE_X] * self.MODEL_SHAPE_SIZE_Y)
            self.model = self.field.copy()
        else:
            self.field = field.copy()
            self.model = field.copy()
        self.stucked = False
        self.positions = np.array(Model.all_models[type_model].copy())
        self.saved_positions = [[], [], [], []]
        self.last_model = []  # grid with model on it in final position
        self.current_positions = 0

        for model_position in range(len(self.positions)):
            for coordinate in self.positions[model_position]:
                row_coordinate = coordinate // self.MODEL_SHAPE_SIZE_X
                column_coordinate = coordinate % self.MODEL_SHAPE_SIZE_X
                #print('row_coordinate is ', row_coordinate, 'column_coordinate is ', column_coordinate)
                #print(self.model)
                if self.model[row_coordinate][column_coordinate] != 0:
                    self.model[row_coordinate][column_coordinate] = 0
                else:
                    self.check_gameover()
            self.saved_positions[model_position] = self.model
            self.model = self.field.copy()

    def draw(self):
        # переводим из однозначной координаты в двузначную координату
        for model_position in range(len(self.positions)):
            for coordinate in self.positions[model_position]:
                row_coordinate = coordinate // self.MODEL_SHAPE_SIZE_X
                column_coordinate = coordinate % self.MODEL_SHAPE_SIZE_X

                # если не выходим за границы
                if row_coordinate < self.MODEL_SHAPE_SIZE_Y and column_coordinate < self.MODEL_SHAPE_SIZE_X:
                    if self.model[row_coordinate][column_coordinate] != 0:
                        #print('row_coordinate is ', row_coordinate, 'column_coordinate is ', column_coordinate)
                        self.model[row_coordinate][column_coordinate] = 0
                        self.last_model = self.saved_positions[self.current_positions].copy()
                else:  # если выходим за границы
                    self.last_model = self.saved_positions[self.current_positions]
                    if row_coordinate >= self.MODEL_SHAPE_SIZE_Y and column_coordinate < self.MODEL_SHAPE_SIZE_X:
                        self.model[self.MODEL_SHAPE_SIZE_Y - 1][self.MODEL_SHAPE_SIZE_X - 1] = 0
                    elif row_coordinate >= self.MODEL_SHAPE_SIZE_Y:
                        self.model[self.MODEL_SHAPE_SIZE_Y - 1][column_coordinate] = 0
                    elif column_coordinate >= self.MODEL_SHAPE_SIZE_X:
                        self.model[row_coordinate][self.MODEL_SHAPE_SIZE_X - 1] = 0
            self.saved_positions[model_position] = self.model
            self.model = self.field.copy()

    def freeze_model(self):
        if np.any((self.positions[self.current_positions]) > self.MODEL_SHAPE_SIZE_X * (
                self.MODEL_SHAPE_SIZE_Y - 1) - 1):  # если модель коснулась последней строки
            self.last_model = self.saved_positions[self.current_positions]
            print('model freezed')
            np.append(Model.storage_freezed, self.positions[self.current_positions])
            for i in self.positions[self.current_positions]:
                Model.storage_freezed.add(i)
            print(Model.storage_freezed)
            self.stucked = True
            return
        return False

    def move_down(self):
        if not self.bottom_reached() and not check_obst(Model.storage_freezed,
                                                        self.positions[self.current_positions].copy() + 10):  # AND
            for i in self.positions:
                i += 10
            self.draw()
        else:
            self.freeze_model()
            self.stucked = True
            for i in self.positions[self.current_positions]:
                Model.storage_freezed.add(i)

        print(self.positions[self.current_positions])
        print(Model.storage_freezed)
        self.print_out()

    def move_right(self):
        if not self.right_boundaries_reached():
            for i in self.positions:
                for j in range(len(i)):
                    if i[j] % 10 == 9:
                        i[j] -= 9
                    else:
                        i[j] += 1
        self.move_down()

    def move_left(self):
        if not self.left_boundaries_reached():
            for i in self.positions:
                for j in range(len(i)):
                    if i[j] % 10 == 0:
                        i[j] += 9
                    else:
                        i[j] -= 1
        self.move_down()

    def rotate(self):
        if not self.bottom_reached():
            if self.current_positions < 3:
                self.current_positions += 1
            else:
                self.current_positions = 0
            self.move_down()
        else:
            self.print_out()

    def print_out(self):
        for i in self.saved_positions[self.current_positions]:
            print(' '.join(map(str, i)))

    def bottom_reached(self):
        if np.any(
                (self.positions[self.current_positions]) > self.MODEL_SHAPE_SIZE_X * (self.MODEL_SHAPE_SIZE_Y - 1) - 1):
            print('bottom is reached!')
            return True
        return False

    def left_boundaries_reached(self):
        if np.any(((self.positions[self.current_positions])) % 10 == 0) or check_obst(Model.storage_freezed,
                                                                                      self.positions[
                                                                                          self.current_positions].copy() + 9): #-1
            print('left boundary is reached!')
            return True
        return False

    def right_boundaries_reached(self):
        if np.any(((self.positions[self.current_positions])) % 10 == 9) or check_obst(Model.storage_freezed,
                                                                                      self.positions[
                                                                                          self.current_positions].copy() + 11): # +1
            print('right boundary is reached!')
            return True
        return False

    def check_gameover(self):
        _count = 0
        for i in range(self.MODEL_SHAPE_SIZE_X):
            if np.count_nonzero(self.saved_positions[self.current_positions][:, i] == 0) >= self.MODEL_SHAPE_SIZE_Y:
                return print('Game over!')
        for j in range(10):
            for i in Model.storage_freezed:
                if i % 10 == j:
                    _count += 1
            if _count == 10:
                print()
                print('Game over!')
                return True
            else:
                _count = 0
        return False



def check_obst(obst, to_check):
    for i in obst:
        for j in to_check:
            if np.any(i == j):
                return True
    return False


type_of_model = input('Choose the model    ').split()
dimensions = input('Choose the size of playground    ').split()

obj_model = Model(type_model=type_of_model[0], MODEL_SHAPE_SIZE_X=int(dimensions[0]),
                  MODEL_SHAPE_SIZE_Y=int(dimensions[1]))

field = []
print()
for i in obj_model.model:
    print(' '.join(map(str, i)))
print()
obj_model.print_out()
while not obj_model.check_gameover():
    obj_model.check_gameover()
    obj_model.freeze_model()
    if obj_model.stucked:
        type_of_model = input('Choose the model    ').split()
        glob_field = obj_model.last_model.copy()
        obj_model = Model(type_model=type_of_model[0], MODEL_SHAPE_SIZE_X=int(dimensions[0]),
                          MODEL_SHAPE_SIZE_Y=int(dimensions[1]), field=glob_field.copy())
        obj_model.print_out()
    else:
        cmd = input('what to do?  left? right? rotate? down?   ')
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
