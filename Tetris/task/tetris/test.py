import numpy as np

a = [[0,1,3], [0,2,1], [0,2,3]]
#a = [1,1,3]
a = np.array(a)
print(np.count_nonzero(a[:,0]==0))
b = {1, 1, 3}
for i in b:
    for z in a:
        for j in z:
            if i == j:
                print('found!', i)
