#인코딩되며 숫자의 크기에 따라 가중치가 더 부여되거나 중요하게 인식될 가능성이 있음
#그래서 레이블 인코딩은 선형 회귀와 같은 ML 알고리즘에는 적용 X
#트리 계열의 ML 알고리즘은 숫자의 특성을 반영하지 않아 레이블 인코딩 사용 가능
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import numpy as np

items = ['TV', '냉장고', '전자레인지', '컴퓨터', '선풍기', '선풍기', '믹서', '믹서']

#LabelEncoder를 객체로 생성한 후 fit()과 transform()으로 레이블 인코딩 수행
encoder = LabelEncoder()
encoder.fit(items)
labels = encoder.transform(items)
print('인코딩 변환값 : ', labels)

print('인코딩 클래스 : ', encoder.classes_)

print('디코딩 원본값 : ', encoder.inverse_transform([0, 1, 4, 5, 3, 3, 2, 2]))

#OneHotEncoder 사용
#먼저 숫자값으로 변환을 위해 LabelEncoder로 변환
print('##원핫인코딩##')
encoder = LabelEncoder()
encoder.fit(items)
labels = encoder.transform(items)
# print(labels)

#2차원 데이터로 변환
labels = labels.reshape(-1,1)
# print(labels)

#원핫 인코딩 적용
oh_encoder = OneHotEncoder()
oh_encoder.fit(labels)
oh_labels = oh_encoder.transform(labels)
print('원핫 인코딩 데이터')
print(oh_labels.toarray())
print('원핫 인코딩 데이터 차원')
print(oh_labels.shape)

#pandas에서 get_dummies() 이용하기
import pandas as pd

df = pd.DataFrame(items, columns = ['items'])
print(pd.get_dummies(df))