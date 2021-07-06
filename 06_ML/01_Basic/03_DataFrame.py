import pandas as pd

'''
DataFrame 혼동 방지를 위한 3가지 가이드

1. DataFrame 뒤의 []는 numpy, Series의 []와 다르다
2. DataFrame 뒤의 [] 내 입력값은 컬럼명(또는 컬럼 리스트) or 불린 인덱스 용도로만 사용
3. DataFrame[0:3]과 같은 슬라이싱 연산 사용 지양
'''

titanic_df = pd.read_csv('train.csv')
print(titanic_df['Pclass'].head(3))
print(titanic_df[['Survived', 'Pclass']].head(3)) #리스트로 출력 컬럼을 묶어준 후 입력
# print(titanic_df[0].head()) #error
print(titanic_df[0:2]) #슬라이싱을 사용해 행데이터를 가져오는건 가능 / 사용 지양

#Boolean 인덱싱 가능
print(titanic_df[titanic_df['Pclass'] ==3 ].head(3)) #Pclass의 값이 3인 데이터 3개 추출
print()
print()

####
#iloc, loc
print('#####iloc, loc#####')


data = {'Name' : ['kang','seo','kim','park'],
           'Year' : [2011,2016,2015,2015],
           'Gender' : ['M','F','M','M']
}
data_df = pd.DataFrame(data, index = ['one','two','three','four'])
print(data_df)

#iloc
print(data_df.iloc[0,0])
# print(data_df.iloc[0,'Name']) #error #인덱싱이 아닌 명칭을 입력해 오류 발생

#loc
print(data_df.loc['one','Name'])

#정리
print('위치 기반 iloc slicing\n', data_df.iloc[0:1, 0],'\n')
print('명칭 기반 loc slicing\n', data_df.loc['one':'two','Name'],'\n')
print()
print()

######
#Boolean indexing
print('#####Boolean indexing#####')
titanic_boolean = titanic_df[titanic_df['Age']>60]
print(type(titanic_boolean))
print(titanic_boolean.head())

#60세 이상 승객 이름,나이만 출력
print(titanic_df[titanic_df['Age']>60][['Name', 'Age']].head())

#위의 예를 loc 사용
print(titanic_df.loc[titanic_df['Age']>60,['Name', 'Age']].head())

#and 조건일때는 & / or 조건일때는 \ / not 조건일때는 ~
print(titanic_df[(titanic_df['Age']>60) & (titanic_df['Pclass']==1) & (titanic_df['Sex'] == 'female')].head())

