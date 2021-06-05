#리스트의 복사

#얕은 복사(shallow copy)(같은 주소를 가르킴)
scores= [65,70,90,89,78]
value = scores

print('scores : ',scores)
print('value : ',value)

scores[3] = 98
print('scores 값 변경 : ',scores)
print('value 값 변경 : ',value)

value[0] = 100
print('scores 값 변경 : ',scores)
print('value 값 변경 : ',value)

# 깊은 복사(deep copy)
value2 = scores.copy()
print('value2 : ',value2)
scores[0] = 50

print('scores : ',scores)
print('value : ',value)
print('value2 : ',value2)


value3 = list(scores)
print('value3 : ',value3)
scores[0] = 150
print('scores : ',scores)
print('value : ',value)
print('value2 : ',value2)
print('value3 : ',value3)

import copy

value4 = copy.deepcopy(scores)
scores[0] = 1000
print('scores : ',scores)
print('value : ',value)
print('value2 : ',value2)
print('value3 : ',value3)
print('value4 : ',value4)
