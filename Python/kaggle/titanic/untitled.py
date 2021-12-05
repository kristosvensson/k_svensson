#!/usr/local/bin/python3.9

## Read libraries and training data
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

train_df = pd.read_csv("data/train.csv")
test_df = pd.read_csv("data/test.csv")

print(train_df.head())


## Data exploration
print(train_df.info())

### Survived vs sex
plt.subplot(121)
plt.hist(train_df.loc[train_df['Sex'] == 'male']['Survived'], bins = 2)
plt.grid(True)
plt.title('Male')

plt.subplot(122)
plt.hist(train_df.loc[train_df['Sex'] == 'female']['Survived'], bins = 2)
plt.grid(True)
plt.title('Female')

plt.show()

### Survived vs age
train_df.boxplot(column = 'Age', by = 'Survived')
plt.title('Age vs. Survival')
plt.show()

### Survived vs class
plt.subplot(131)
plt.hist(train_df.loc[train_df['Pclass'] == 1]['Survived'], bins = 2)
plt.grid(True)
plt.title('1st class')

plt.subplot(132)
plt.hist(train_df.loc[train_df['Pclass'] == 2]['Survived'], bins = 2)
plt.grid(True)
plt.title('2nd class')

plt.subplot(133)
plt.hist(train_df.loc[train_df['Pclass'] == 3]['Survived'], bins = 2)
plt.grid(True)
plt.title('3rd class')

plt.show()

### Survived vs age
train_df.boxplot(column = 'SibSp', by = 'Survived')
plt.title('SibSp vs. Survival')
plt.show()

## Mutate new columns - 'age group' and 'alone'
train_df['Age_group'] = train_df['Age'].apply(lambda x: 'child' if x < 10 else( 'teen' if x < 20  else( 'adult' if x < 70 else 'elder' )))
print(train_df)

### plot survived by age group
stacked_data = pd.pivot_table(train_df.loc[:,['Survived','Age_group']], index=['Survived'], columns=['Age_group'], aggfunc=len)
stacked_data.transpose().apply(lambda x: x*100/sum(x), axis=1).loc[['child','teen','adult','elder'],:].plot(kind="bar", stacked=True)
plt.show()

### print survived by gender
men_survived = train_df[(train_df['Sex']=='male')&(train_df['Survived']==1)]['Survived'].count()
men_total = train_df[train_df['Sex']=='male']['Survived'].count()
share_men_survived = men_survived / men_total
print("share of men in training data that survived: ", share_men_survived)

female_survived = train_df[(train_df['Sex']=='female')&(train_df['Survived']==1)]['Survived'].count()
female_total = train_df[train_df['Sex']=='female']['Survived'].count()
share_female_survived = female_survived / female_total
print("share of women in training data that survived: ", share_female_survived)

## Fill missing values
def fill_na_int(data, column):
    data[column] = data[column].fillna(round(data[column].std() * np.random.randn() + data[column].mean()))
    return data

def fill_na_str(data, column):
    data[column] = data[column].fillna(str(data[column].mode()))
    return data


train_df = fill_na_int(train_df,'Age')
train_df = fill_na_str(train_df, 'Embarked')

print(train_df.count())






# Try it with keras:
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

