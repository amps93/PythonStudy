import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

titanic_df = pd.read_csv('train.csv')
# print(titanic_df.info())

#결측치 제거
titanic_df['Age'].fillna(titanic_df['Age'].mean(), inplace=True)
titanic_df['Cabin'].fillna('N', inplace=True)
titanic_df['Embarked'].fillna('N', inplace=True)
print('데이터 세트 null 값 개수 : ', titanic_df.isnull().sum().sum())

#문자열 값 분포 살펴보기
print('Sex 값 분포 :\n', titanic_df['Sex'].value_counts())
print('\nCabin 값 분포 :\n', titanic_df['Cabin'].value_counts())
print('\nSex 값 분포 :\n', titanic_df['Embarked'].value_counts())

titanic_df['Cabin'] = titanic_df['Cabin'].str[:1]
print(titanic_df['Cabin'].head())

#성별과 생존자간의 관계
print(titanic_df.groupby(['Sex', 'Survived'])['Survived'].count())

#barplot 그리기
sns.barplot(x='Sex', y='Survived', data=titanic_df)
plt.show()

sns.barplot(x='Pclass', y='Survived', hue='Sex', data=titanic_df)
plt.show()

#입력 age에 따라 구분 값을 반환하는 함수 설정. DataFrame의 apply lambda 사용
def get_category(age):
    cat = ''
    if age <= -1: cat = 'Unkown'
    elif age <= 5 : cat = 'Baby'
    elif age <= 12 : cat = 'Child'
    elif age <= 18 : cat = 'Teenager'
    elif age <= 25 : cat = 'Student'
    elif age <= 35 : cat = 'Young Adult'
    elif age <= 60 : cat = 'Adult'
    else: cat = 'Elderly'

    return cat

#막대그래프의 크기 figure를 더 크게 설정
plt.figure(figsize=(10, 6))

#X축의 값을 순차적으로 표시하기 위한 설정
group_names = ['Unkown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Elderly']

#lambda 식에 위에서 생성한 get_category() 함수를 반환값으로 사용
#get_category(x)는 입력값으로 'Age' 컬럼 값을 받아서 해당하는 cat 반환
titanic_df['Age_cat'] = titanic_df['Age'].apply(lambda x : get_category(x))
sns.barplot(x='Age_cat', y='Survived', hue='Sex', data=titanic_df, order=group_names)
plt.show()

titanic_df.drop('Age_cat', axis=1, inplace=True)

from sklearn import preprocessing

#레이블 인코딩 함수
def encode_features(dataDF):
    #문자열 카테고리 피처
    features = ['Cabin', 'Sex', 'Embarked']
    for feature in features:
        le = preprocessing.LabelEncoder()
        le = le.fit(dataDF[feature])
        dataDF[feature] = le.transform(dataDF[feature])
    return dataDF

titanic_df = encode_features(titanic_df)
print(titanic_df.head())

# 지금까지 가공한 내용을 정리하고 함수로 작성(재사용 가능)
from sklearn.preprocessing import LabelEncoder

#Null 처리 함수
def fillna(df):
    df['Age'].fillna(df['Age'].mean(), inplace=True)
    df['Cabin'].fillna('N', inplace=True)
    df['Embarked'].fillna('N', inplace=True)
    df['Fare'].fillna(0, inplace=True)
    return df

#머신러닝 알고리즘에 불필요한 속성 제거
def drop_features(df):
    df.drop(['PassengerId', 'Name', 'Ticket'], axis=1, inplace=True)
    return df


#레이블 인코딩 수행
def format_features(df):
    df['Cabin'] = df['Cabin'].str[:1] #첫문자만 추출
    features = ['Cabin', 'Sex', 'Embarked']
    for feature in features:
        le = preprocessing.LabelEncoder()
        le = le.fit(df[feature])
        df[feature] = le.transform(df[feature])
    return df

#앞에서 설정한 Data Preprocessing 함수 호출
def transform_features(df):
    df = fillna(df)
    df = drop_features(df)
    df = format_features(df)
    return df