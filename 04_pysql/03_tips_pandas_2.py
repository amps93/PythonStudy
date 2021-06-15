#JOIN, UNION, ETC, UPDATE, DELETE
import pandas as pd
import numpy as np

tips = pd.read_csv('tips.csv')

#JOIN
print('*****JOIN*****')
df1 = pd.DataFrame({"key": ["A", "B", "C", "D"], "value": np.random.randn(4)})
df2 = pd.DataFrame({"key": ["B", "D", "D", "E"], "value": np.random.randn(4)})

print('*****INNER JOIN*****')
'''
SELECT *
FROM df1
INNER JOIN df2
  ON df1.key = df2.key;
'''
print('merge함수 사용하여 INNER JOIN 하기(key값 기준으로)')
print(pd.merge(df1, df2, on='key'))

indexed_df2 = df2.set_index("key")
# print(indexed_df2)
print(pd.merge(df1, indexed_df2, left_on="key", right_index=True))
print()

#LEFT JOIN
print('*****LEFT JOIN*****')
'''
-- show all records from df1
SELECT *
FROM df1
LEFT OUTER JOIN df2
  ON df1.key = df2.key;
'''
print('merge함수 사용하여 LEFT JOIN 하기(key값 기준으로)')
print(pd.merge(df1, df2, on="key", how="left"))
print()

#RIGHT JOIN
print('*****RIGHT JOIN*****')
'''
-- show all records from df2
SELECT *
FROM df1
RIGHT OUTER JOIN df2
  ON df1.key = df2.key;
'''
print('merge함수 사용하여 RIGHT JOIN 하기(key값 기준으로)')
print(pd.merge(df1, df2, on="key", how="right"))
print()

#FULL JOIN
print('*****FULL JOIN*****')
'''
-- show all records from both tables
SELECT *
FROM df1
FULL OUTER JOIN df2
  ON df1.key = df2.key;
'''
print('merge함수 사용하여 FULL JOIN 하기(key값 기준으로)')
print(pd.merge(df1, df2, on="key", how="outer"))
print()

#UNION
df1 = pd.DataFrame(
    {"city": ["Chicago", "San Francisco", "New York City"], "rank": range(1, 4)}
)
df2 = pd.DataFrame(
     {"city": ["Chicago", "Boston", "Los Angeles"], "rank": [1, 4, 5]}
)
'''
SELECT city, rank
FROM df1
UNION ALL
SELECT city, rank
FROM df2;
/*
         city  rank
      Chicago     1
San Francisco     2
New York City     3
      Chicago     1
       Boston     4
  Los Angeles     5
*/
'''
print('*****UNION*****')
print('concat 함수 사용하여 UNION 수행하기')
print(pd.concat([df1, df2]))

print('concat 함수 사용하여 UNION ALL 수행하기')
print(pd.concat([df1, df2]).drop_duplicates())
print()

#ETC
print('*****기타 SQL 분석 및 집계 함수 사용하기*****')
'''
SELECT * FROM tips
ORDER BY tip DESC
LIMIT 10 OFFSET 5;
'''
print('nlargest 사용하여 tip 컬럼 15개까지 내림차순 정렬')
print(tips.nlargest(10 + 5, columns="tip"))
print()

'''
-- Oracle's ROW_NUMBER() analytic function
SELECT * FROM (
  SELECT
    t.*,
    ROW_NUMBER() OVER(PARTITION BY day ORDER BY total_bill DESC) AS rn
  FROM tips t
)
WHERE rn < 3
ORDER BY day, rn;
'''
print('Top n rows per group')
print(tips.assign(rn=tips.sort_values(['total_bill'], ascending=False)
                  .groupby(['day'])
                  .cumcount()
                  +1
                )
      .query('rn < 3')
      .sort_values(['day', 'rn'])
)
print()

#UPDATE
print('*****UPDATE*****')
'''
UPDATE tips
SET tip = tip*2
WHERE tip < 2;
'''
print('tip컬럼의 값이 2보다 작으면 2를 곱한 후 UPDATE')
# tips.loc[tips["tip"] < 2, "tip"] *= 2
# print(tips)
print()

#DELETE
print('*****DELETE*****')
'''
DELETE FROM tips
WHERE tip > 9;
'''
print('tip칼럼의 값이 9이하인 값만 남겨둠')
tips = tips.loc[tips["tip"] <= 9]
print(tips)