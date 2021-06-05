import pandas as pd
import pandas_profiling

df = pd.read_csv('tips.csv')
print(df.describe())
print(df.info())
print(df.columns)

#pandas_profiling 활용하여 데이터 요약 자료 생성
# profile = df.profile_report(title="tips")
# profile.to_file(output_file="tips.html") #html파일로 저장