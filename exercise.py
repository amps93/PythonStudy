import numpy as np

a=np.random.rand(3,1)
# print(np.random.rand(3,3))
# print(np.zeros_like(a))

b=np.zeros(1)
print(a)
print(b)

print(np.dot(a,b.T))