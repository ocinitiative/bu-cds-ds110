# # wine.data:  see https://archive.ics.uci.edu/ml/datasets/Wine

import pandas as pd

col_names = ['Type','Alcohol','Malic acid','Ash','Alcalinity of ash',
             'Magnesium','Total phenols','Flavanoids','Nonflavanoid phenols',
             'Proanthocyanins','Color intensity','Hue','OD280/OD315','Proline']

df = pd.read_csv('wine.data', names =col_names)
df.head()

# We then separate the data into features (X) and labels (y).

y = df['Type']
X = df.iloc[:,1:]

# Explain what the next code box is doing, and why it is important to do it for a nearest neighbors classifier training on this data.

for col in range(13):
    X.iloc[:,col] = (X.iloc[:,col]) / (X.iloc[:,col].max())



