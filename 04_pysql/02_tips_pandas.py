#SELECT, WHERE, NULL CHECKING, GROUP BY

import pandas as pd
import numpy as np

tips = pd.read_csv('tips.csv')
print(tips.head())
print()

#SELECT
print('*****SELECT*****')
'''
SELECT total_bill, tip, smoker, time
FROM tips
LIMIT 5;
'''
print(tips[['total_bill', 'tip', 'smoker', 'time']].head())
print()

#WHERE
print('*****WHERE*****')
'''
SELECT * 
FROM tips 
WHERE time = 'Dinner'
LIMIT 5;
'''
print(tips[tips['time'] == 'Dinner'].head())
print()

#time 컬럼의 Dinner이면 True 아니면 False를 준 후 value_counts를 통해 갯수 확인
is_dinner = tips['time'] == 'Dinner'
print(is_dinner.value_counts())
# print(tips[is_dinner].head())
print()

#Dinner 타임에 팁이 5$ 이상인 로우만 출력
'''
SELECT *
FROM tips
WHERE time = 'Dinner' AND tip > 5.00;
'''
print('***time = Dinner ,tips > 5.00$***')
print(tips[(tips['time'] == 'Dinner') & (tips['tip'] > 5.00)])
print()

#Null checking
print('***Null값 확인***')
frame = pd.DataFrame(
    {"col1": ["A", "B", np.NaN, "C", "D"], "col2": ["F", np.NaN, "G", "H", "I"]}
)
# print(frame)
'''
SELECT *
FROM frame
WHERE col1 IS NOT NULL;
'''
print(frame[frame["col1"].isna()])
print(frame[frame["col2"].isna()])
print('***col1에서 Null값 없는 데이터 출력***')
print(frame[frame["col1"].notna()])
print()

#GROUP BY
print('*****GROUP BY*****')
'''
SELECT sex, count(*)
FROM tips
GROUP BY sex;
/*
Female     87
Male      157
*/
'''
print('***성별 카운트1***')
print(tips.groupby("sex").size())
print('***성별 카운트2***')
print(tips.groupby("sex")["total_bill"].count())
print('***성별에 따른 다른 컬럼 카운트***')
print(tips.groupby("sex").count())
print()

#Multiple fuction
'''
SELECT day, AVG(tip), COUNT(*)
FROM tips
GROUP BY day;
/*
Fri   2.734737   19
Sat   2.993103   87
Sun   3.255132   76
Thur  2.771452   62
*/
'''
print('***확장된 GROUP BY(agg 사용)***')
print(tips.groupby("day").agg({"tip": np.mean, "day": np.size}))
print()

#3차원 데이터 프레임
'''
SELECT smoker, day, COUNT(*), AVG(tip)
FROM tips
GROUP BY smoker, day;
/*
smoker day
No     Fri      4  2.812500
       Sat     45  3.102889
       Sun     57  3.167895
       Thur    45  2.673778
Yes    Fri     15  2.714000
       Sat     42  2.875476
       Sun     19  3.516842
       Thur    17  3.030000
*/
'''
print('***GROUP BY로 3차원 데이터 프레임 만들기***')
print(tips.groupby(["smoker", "day"]).agg({"tip": [np.size, np.mean]}))