import pandas as pd
data={'Age' : [69,96,58,24],
    'Money': [20000,25000,68000,98050]}

df=pd.DataFrame(data)
print(df)

mean_age= df['Age'].mean()
print(f"Mean : {mean_age}")

median_money = df['Money'].median()
print(f"Median : {median_money}")

std_age = df['Age'].std()
print(f"Std : {std_age}")