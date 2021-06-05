import pandas as pd

data = [
    ['Belgium', 'Brussels', 11190846],
    ['India', 'New Delhi', 1303171035],
    ['Brazil', 'Brasilia', 207847528]
]

df = pd.DataFrame(data)
print(df)
print('-'*35)

df = pd.DataFrame(data, columns=['Country', 'Capital', 'Population'])
print(df)
print(df['Country'])
print(df.Country) #위 결과와 동일
print('-'*35)

#dictionary로 DataFrame에 데이터 넘겨주기
data = {
    'Country' : ['Belgium', 'Brussels', 11190846],
    'Capital' : ['India', 'New Delhi', 1303171035],
    'Population' : ['Brazil', 'Brasilia', 207847528]
}

df = pd.DataFrame(data)
print(df)
print('*****info*****')
print(df.info())
print('*****index*****')
print(df.index)
print('*****columns*****')
print(df.columns)
print('*****dtypes*****')
print(df.dtypes)
print('*****values*****')
print(df.values)

s_1 = pd.Series([1, 2, 3, 4], index=['A', 'B', 'C', 'D'])
s_2 = pd.Series([5, 6, 7, 8], index=['A', 'B', 'C', 'D'])
s_3 = pd.Series([9, 10, 11, 12], index=['A', 'B', 'C', 'D'])

data = {'col1': s_1,
        'col2': s_2,
        'col3': s_3}

df_4 = pd.DataFrame(data, index=['A', 'B', 'C', 'D'])

print(df_4)