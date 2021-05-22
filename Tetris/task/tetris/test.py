import numpy as np

a = [[1,1,3], [3,2,1], [5,2,3]]
#a = [1,1,3]
a = np.array(a)
b = {1, 1, 3}
for i in b:
    for z in a:
        for j in z:
            if i == j:
                print('found!', i)
