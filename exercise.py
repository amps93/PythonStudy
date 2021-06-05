import pandas as pd

# s_1 = pd.Series([1, 2, 3, 4], index=['A', 'B', 'C', 'D'])
# s_2 = pd.Series([5, 6, 7, 8], index=['A', 'B', 'C', 'D'])
# s_3 = pd.Series([9, 10, 11, 12], index=['A', 'B', 'C', 'D'])

s_1 = pd.Series([1, 2, 3, 4])
s_2 = pd.Series([5, 6, 7, 8])
s_3 = pd.Series([9, 10, 11, 12])

print(s_3)
data = {'col1': s_1,
        'col2': s_2,
        'col3': s_3}
print(data)
print('-------------------')
data = {'col1': [1,2,3,4],
        'col2': [5,6,7,8],
        'col3': [9,10,21,12]}
print(data)
# df_4 = pd.DataFrame(data, index=['A', 'B', 'C', 'D'])
#
# print(df_4)