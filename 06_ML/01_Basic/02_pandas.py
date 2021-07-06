import pandas as pd

titanic_df = pd.read_csv('train.csv')
#DF의 기본 정보 확인
# print(titanic_df.head(3))
# print(titanic_df.shape)
# print(titanic_df.info())
# print(titanic_df.describe())

#value_counts : Series 데이터 타입에서만 사용 가능 (DF는 불가)
# print(titanic_df['Pclass'][0:5])
# print(titanic_df['Pclass'].value_counts())
# titanic_pclass = titanic_df['Pclass']
# print(titanic_pclass.head())

#DF 컬럼 생성과 수정
#기존 컬럼 활용하여 Age_by_10, Family_No 컬럼 생성
# titanic_df['Age_by_10'] = titanic_df['Age']*10
# titanic_df['Family_No'] = titanic_df['SibSp'] + titanic_df['Parch']+1
# print(titanic_df.head())
#Age_by_10 컬럼 수정
# titanic_df['Age_by_10'] = titanic_df['Age_by_10']+100
# print(titanic_df.head())

#DF 데이터 삭제
# print(titanic_df.head())
# titanic_drop_df = titanic_df.drop('Age_by_10', axis=1)
# print(titanic_drop_df.head())

#DF Row 값 삭제
#inplace : 변수에 새로 할당하지 않고 기존 DF에 바로 적용
# titanic_df.drop([0,1,2], axis = 0, inplace=True)
# print(titanic_df.head())

#Index 객체
# indexes = titanic_df.index
# print(indexes)
# print('index 객체 array값 :\n', indexes.values)
# print(type(indexes.values))
# print(indexes.values.shape)
# print(indexes[:5].values)
# print(indexes.values[:5])
# print(indexes[6])

#index of DF or Seires cannot be changed
# indexes[0] = 5 #error

#reset_index() : DF 또는 Series에 새로운 인덱스를 연속 숫자형으로 할당하며 기존 인덱스는 index라는 새로운 컬럼으로 추가됨
print(titanic_df.reset_index(inplace=False))