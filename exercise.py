numData = \
    [
        [5, 7, -5, 100, 73],
        [35, 23, 4, 190, 33],
        [49, 85, 662, 39, 81],
        [124, -59, 86, 46, 52],
        [27, 7, 8, 33, -56]
    ]
a=[]
for i in numData:
    for j in i:
        a.append(abs(j))

for i in range(len(a)):
    if a[i]>100:
        a[i] = a[i]%100

import numpy as np
a = np.array(a)
print(a.reshape(5,5))
