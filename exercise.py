import pandas as pd
data = [
    ['Ali',
     'Azmat',
     '30'],
    ['Sharukh',
     'Khan',
     '40'],
    ['Linus',
     'Torvalds',
     '70']
]
df = pd.DataFrame(data,columns=['First','Last','Age'])
print (df)
print()

df = pd.DataFrame(data,columns=['First','Last','Age'])
df["Full Name"] = df["First"] + " " + df["Last"]
print(df)
print()

df = pd.DataFrame(data,columns=['First','Last','Age'])
df["Full Name"] = df["First"].map(str) + " " + df["Last"]
print(df)