import numpy as np

array1 = np.arange(10)
print('array1 :\n', array1)

array2 = array1.reshape(2,5)
print('array2 : \n', array2)

array3 = array1.reshape(5,2)
print('array3 : \n', array3)

# -1 사용하기
# -1을 인자로 사용하면 원래 ndarray와 호환되는 새로운 shape로 변환해줌
array4 = array1.reshape(-1,5)
print('array4 : \n', array4)
print('array4 shape : ', array4.shape)

array5 = array1.reshape((5,-1))
print('array5 : \n', array5)
print('array5 shape : ', array5.shape)