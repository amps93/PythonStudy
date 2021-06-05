import numpy as np

a = [[1, 2, 3], [4, 5, 6]]
print(a)
b = np.array(a)
print(b)

print('dtype : ', b.dtype)
print('ndim : ', b.ndim)
print('shape : ', b.shape)

c = np.array([[1, 1, 1], [2, 2, 2]], dtype='float64')
print(c)

print(b+c)
print(b-c)
print(b*c)
print(b/c)

#strides : 배열을 탐색할때 각 차원에서 단계별로 이동할 바이트 수
print('strides : ', c.strides)  #(24, 8) : 다음 열로 이동하려면 8바이트(1개 값)를 건너 뛰고 다음행에서 같은 위치에 도달하려면 24바이트(3개 값)를 건너 뛰어야 함

print('axis = 0 : ', c.sum(axis=0)) #열의 합
print('axis = 1 : ', c.sum(axis=1)) #행의 합
# strides , reshape zeros axis eyes ones
print('zeros : \n', np.zeros((3,3)))
print('ones : \n', np.ones((3,3)))
print('eye : \n', np.eye(3))

#reshape
print('reshape')
print(np.reshape(c, (3,2)))
print(c.reshape(3,2))
#reshape -1
x = np.arange(12)
x = x.reshape(3,4)
#행의 위치에 -1을 넣고 열의 값을 지정해주면 행의 수는 알아서 지정됨
print(x.reshape(-1,1))
print(x.reshape(-1,2))
print(x.reshape(-1,3))

#열의 위치에 -1을 넣고 행의 값을 지정해주면 열의 수는 알아서 지정됨
print(x.reshape(1,-1))
print(x.reshape(2,-1))
print(x.reshape(3,-1))

#행렬의 곱 : a.dot(b) or np.dat(a,b)
#전치행렬 : a.transpose() or np.transpose(a)
#역행렬 : np.linalg.inv(a)
#행렬식 : np.linalg.det(a)
