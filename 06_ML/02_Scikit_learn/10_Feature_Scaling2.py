#Scaling 유의점

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler

#학습 데이터는 0~10, 테스트 데이터는 0~5 값을 가지는 데이터 생성
#Scaler 클래스의 fit(), transform()은 2차원 이상 데이터만 가능하므로 reshape(-1,1)로 차원 변환
train_array = np.arange(0, 11).reshape(-1, 1)
test_array = np.arange(0, 6).reshape(-1, 1)

#MinMaxScaler 객체에 별도의 feature_range 파라미터 값을 지정하지 않으면 0~1 값으로 변환
scaler = MinMaxScaler()

#fit()하게 되면 train_array 데이터의 최솟값이 0, 최댓값이 10으로 지정
scaler.fit(train_array)

#1/10 scale로 train_array 데이터 변환함. 원본 10 -> 1로 변환됨
train_scaled = scaler.transform(train_array)

print('원본 train_array 데이터 : ', np.round(train_array.reshape(-1), 2))
print('Salce된 train_array 데이터 : ', np.round(train_scaled.reshape(-1), 2))

#MinMaxScaler에 test_array를 fit()하게 되면 원본 데이터의 최솟값이 0, 최댓값이 5로 설정됨
scaler.fit(test_array)

#1/5 scale로 test_array 데이터 변환함. 원본 5 -> 1로 변환됨
test_scaled = scaler.transform(test_array)

#test_array 의 scale 변환 출력
print('원본 test_array 데이터 : ', np.round(test_array.reshape(-1), 2))
print('Salce된 test_array 데이터 : ', np.round(test_scaled.reshape(-1), 2))
print()

'''
train_array와 test_array의 값이 동일하지 않으나 scale 시 
학습데이터와 테스트데이터의 서로 다른 원본값이 동일한 값으로 변환되는 결과를 초래 (테스트 : 1 -> 0.2 / 학습 : 2 -> 0.2)
따라서 테스트데이터에 다시fit()을 적용해서는 안되며 학습데이터로 이미 fit()이 적용된 Scaler 객체를 사용해 transform()으로 변환해야 함
'''

#올바른 방법
print('개선된 방법')
scaler = MinMaxScaler()
scaler.fit(train_array)
train_scaled = scaler.transform(train_array)
print('원본 train_array 데이터 : ', np.round(train_array.reshape(-1), 2))
print('Scale된 train_array 데이터 : ', np.round(train_scaled.reshape(-1), 2))

#test_array에 Scale 변환을 할 때는 반드시 fit()을 호출하지 않고 transform()만으로 변환해야 함
#위에서 한 fit() 과정이 생략됨
test_scaled = scaler.transform(test_array)
print('원본 test_array 데이터 : ', np.round(test_array.reshape(-1), 2))
print('Salce된 test_array 데이터 : ', np.round(test_scaled.reshape(-1), 2))
