import pandas as pd

df = pd.read_csv('marks.csv')


print(df)

print(df.head())

print(df.info())

print(df.describe())

print(df.sort_index())

print(df.reset_index())

print(df.tail())

print(df.nsmallest(3, 'Marks'))

print(df.nlargest(3, 'Marks'))

print(df.sort_values(by='Marks', ascending=True))