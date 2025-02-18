import pandas as pd

print('Hello world')

data = {
    "calories": [420,380,390,400,410,420,430,440,450,460],
    "duration": [50,40,45,50,55,60,65,70,75,80],
}

df = pd.DataFrame(data)

print(df)

print(df.head)

print(df.loc[0])

df = pd.read_csv("marks.csv")

print(df.head)

df.pivot(columns='10', values='2')
print(df)