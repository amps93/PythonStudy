from sklearn.datasets import load_iris
# 데이터셋 살펴보기

iris_data = load_iris()
print(type(iris_data))

keys = iris_data.keys()
print('붓꽃 데이터 세트의 키들 : ', keys)

print('\n feature_name의 type : ',type(iris_data.feature_names))
print('feature_name의 shape : ',len(iris_data.feature_names))
print(iris_data.feature_names)

print('\n target_name의 type : ',type(iris_data.target_names))
print(' target_name의 shape : ',len(iris_data.target_names))
print(iris_data.target_names)

print('\n data의 type : ',type(iris_data.data))
print(' data의 shape : ',iris_data.data.shape)
print(iris_data.data[0:5])

print('\n target의 type : ',type(iris_data.target))
print(' target의 shape : ',iris_data.target.shape)
print(iris_data.target)

