import pandas as pd

#lambda
def get_square(a):
    return a**2
print(get_square(3))

# lambda 입력인자 : 계산식
lambda_square = lambda x : x**2
print(lambda_square(3))

#map과 활용
a = [1,2,3]
squares = map(lambda x : x**2, a)
print(list(squares))

#apply
titanic_df = pd.read_csv('train.csv')

titanic_df['Name_len'] = titanic_df['Name'].apply(lambda x : len(x))
print(titanic_df[['Name', 'Name_len']].head())

#lambda에 if 사용
#lambda에서 if 사용시 if식보다 반환값을 먼저 기술해야함
titanic_df['Child_Adult'] = titanic_df['Age'].apply(lambda x : 'Child' if x <= 15 else 'Adult')
print(titanic_df[['Age', 'Child_Adult']].head(8))

#lambda에서는 elif를 지원하지 않음
#elif를 적용하려면 else절을 ()로 내포해 ()내에 다시 if else를 사용해야함
titanic_df['Age_cat'] = titanic_df['Age'].apply(lambda x : 'Child' if x <= 15 else ('Adult' if x <= 60 else 'Elderly'))
print(titanic_df['Age_cat'].value_counts())
