# Problem 2: Random Forests

# For this exercise, we'll try using random forests to predict wine quality.  The dataset is from the UCI Machine Learning repository, and rates wines on a scale from 1 to 10.  To turn this into a binary classification problem, we are just interested in identifying wines with a quality score of 7 or more.

import pandas as pd

df = pd.read_csv('winequality-red.csv', sep = ';')
df.head()

# To help make things easier, below we've turned the final column into a *target* vector and created a DataFrame *features* that consists of all the other columns.

target = df['quality'] >= 7
features = df.iloc[:,0:11]

# Now, let's separate the features and target vector into training and testing data with scikit-learn's *train_test_split()* function.

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size = 0.2, random_state = 123, stratify = target)

# Use the RandomForestClassifier of sklearn.ensemble to create a random forest with 200 trees. 
# Train on the training data with *fit()*, and test on the test data with *score()*.

from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(n_estimators = 200, random_state = 123)
rf.fit(X_train, y_train)
rf.score(X_test, y_test)

# The random forest classifier has a *feature_importances_* attribute that gives the relative importance of each feature.  Use this to create a bar plot of the feature importances.

import matplotlib.pyplot as plt

plt.barh(features.columns, rf.feature_importances_)
plt.xlabel('Feature Importance')
plt.ylabel('Feature')
plt.show()

# The random forest classifier also has a *predict()* method that can be used to predict the class of a new sample.  Use this to predict the class of the first 10 samples in the test set.

rf.predict(X_test.iloc[0:10,:])

# Finally, use the *predict_proba()* method to predict the probability of each class for the first 10 samples in the test set.

rf.predict_proba(X_test.iloc[0:10,:])

# Run an experiment in which you find the average test score over 100 trials for a scikit-learn decision tree classifier trained on the wine quality data.

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

scores = []
for i in range(100):
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size = 0.2, random_state = i, stratify = target)
    dt = DecisionTreeClassifier(random_state = i)
    dt.fit(X_train, y_train)
    y_pred = dt.predict(X_test)
    scores.append(accuracy_score(y_test, y_pred))

print('Average test score: {:.3f}'.format(sum(scores)/len(scores)))

# Run an experiment in which you find the average test score over 100 trials for a scikit-learn random forest classifier trained on the wine quality data.

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

scores = []
for i in range(100):
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size = 0.2, random_state = i, stratify = target)
    rf = RandomForestClassifier(n_estimators = 200, random_state = i)
    rf.fit(X_train, y_train)
    y_pred = rf.predict(X_test)
    scores.append(accuracy_score(y_test, y_pred))

print('Average test score: {:.3f}'.format(sum(scores)/len(scores)))

# Run an experiment in which you find the average test score over 100 trials for a scikit-learn logistic regression classifier trained on the wine quality data.









