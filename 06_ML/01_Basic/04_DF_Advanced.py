import pandas as pd

titanic_df = pd.read_csv('train.csv')
# print(titanic_df['Pclass'].value_counts())
#생략된 열 보이게 하는 코드
# pd.options.display.max_columns = None

#정렬
#sort_values()
print('### sort_values()')
titanic_sorted = titanic_df.sort_values(by=['Name'])
print('오름차순 정렬\n', titanic_sorted['Name'])
print()

titanic_sorted = titanic_df.sort_values(by=['Pclass','Name'], ascending=False) #내림차순 정렬
print('내림차순 정렬\n', titanic_sorted['Name'])
print()

#Aggregation
#min(), max(), count() ,sum() 등
print('### count()')
print(titanic_df.count())
print('### mean()')
print(titanic_df[['Age','Fare']].mean())
print()

#groupby()
print('### groupby()')
titanic_groupby = titanic_df.groupby(by='Pclass')
print(type(titanic_groupby))

#Pclass 기준으로 Pclass를 제외한 모든 칼럼 count
titanic_groupby = titanic_df.groupby('Pclass').count()
print(titanic_groupby)

#Pclass 기준으로 ['PassengerId','Survived'] count 후 컬럼 출력
titanic_groupby = titanic_df.groupby('Pclass')[['PassengerId','Survived']].count()
print(titanic_groupby)

#Pclass 기준으로 Age 데이터의 최댓값과 최솟값 출력
print(titanic_df.groupby('Pclass')['Age'].agg([max,min]))

#연산자 dictionary에 저장하여 활용
agg_format = {'Age' : 'max', 'SibSp' : 'sum', 'Fare' : 'mean'}
print(titanic_df.groupby('Pclass').agg(agg_format))
print()

#결손 데이터 처리하기
print('### isna()')
print(titanic_df.isna().head())
print(titanic_df.isna().sum())

print('### fillna()')
titanic_df['Cabin'] = titanic_df['Cabin'].fillna('C000')
print(titanic_df.head())

titanic_df['Age'] = titanic_df['Age'].fillna(titanic_df['Age'].mean())
titanic_df['Embarked'] = titanic_df['Embarked'].fillna('S')
print(titanic_df.isna().sum())