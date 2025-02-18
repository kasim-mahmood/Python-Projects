# Adds the pandas and sklearn library
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Adds the CSV into the vriable 'df'
df = pd.read_csv('music.csv')

# Removes the column 'genre'
X = df.drop(columns=['genre'])

# Variable with only the column 'genre'
Y = df['genre']

# Creates test and train data sets
x_train, x_test, y_train, y_test = train_test_split(X,Y, test_size=0.000000000000000000000000000000000001) # 60% of the total data set

# Inputs both variable into DecisionTreeClassifier
model = DecisionTreeClassifier()
model.fit(x_train, y_train)
predictions = model.predict(x_test)
score = accuracy_score(y_test, predictions)
# print(df)
print(predictions)
print(score)
print('\n \n')

# print(model)

print('\n \n')

# print(x)

print('\n \n')

# print(y)