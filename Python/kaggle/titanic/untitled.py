#!/usr/local/bin/python3.8

## Read libraries and training data
import numpy as np
import pandas as pd

train_df = pd.read_csv("data/train.csv")
test_df = pd.read_csv("data/test.csv")

print(train_df)

## Prepare model

from sklearn.ensemble import RandomForestClassifier

X = train_df.loc[:,["Pclass","Sex","Age","SibSp"]]
X = pd.get_dummies(X, "Sex").loc[:,["Pclass","Sex_female","Age","SibSp"]]
X = X.fillna(X.median())

y = train_df["Survived"]

## Model

print(X)

clf = RandomForestClassifier(n_estimators = 10)
clf = clf.fit(X, y)
print(clf.score(X, y))

X_test = test_df.loc[:,["Pclass","Sex","Age","SibSp"]]
X_test = pd.get_dummies(X_test, "Sex").loc[:,["Pclass","Sex_female","Age","SibSp"]]
X_test = X_test.fillna(X.median())

y_test = clf.predict(X_test)

print(y_test)

result = test_df.loc[:,"PassengerId"]
result = pd.DataFrame(result)
result["Survived"] = y_test.tolist()

print(result)

result.to_csv("utdata/random_forest_submission.csv")