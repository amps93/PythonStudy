import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# print(pd.__version__)

# help(pd)
# help(pd.read_csv)
# help(pd.DataFrame)
# pd.DataFrame?

#Series
print('-----Seires-----')
s = pd.Series([3, -5, 7, 4])
print(s)
print(s[0])
s = pd.Series([3, -5, 7, 4], index=['a','b','c','d'])
print(s)
print(type(s))

#Series 속성 : index, values
print(s.index)
print(s.values)

#인덱싱
print(s['a']) #index명으로 조회
print(s[0]) #index 순서로 조회

#딕셔너리와 공통점 차이점
pop_dict = {
    'Germany' : 81.3,
    'Belgium' : 11.3,
    'France' : 64.3,
    'United Kingdom' : 64.9,
    'Netherlands' : 16.9
}

population = pd.Series(pop_dict)

print(pop_dict['France'])
print(population['France'])
#딕셔너리 : KEY 순서가 없음
#Series : index 순서가 있음
print(population[2])
# print(pop_dict[2]) #에러

#Series는 연산 가능
print(population*1000)
# print(pop_dict*1000) #에러