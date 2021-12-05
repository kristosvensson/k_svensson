#!/usr/local/bin/python3.8
import pandas as pd

df = pd.read_csv("advent_of_code_input_1_1.csv", header=None, names = ['depth'])

##### Base
count = 0

for i in range(1, len(df['depth'])):
    if (df.loc[i, 'depth'] > df.loc[i-1, 'depth']):
        count += 1

print('times increased: ', count)

##### Sliding-window
slide_sum = []

for i in range(2, len(df['depth'])):
        df.loc[i, 'slide'] = df.loc[i, 'depth']+df.loc[i-1, 'depth']+df.loc[i-2, 'depth']

print(df['slide'])

count = 0
        
for i in range(1, len(df['slide'])):
    if (df.loc[i, 'slide'] > df.loc[i-1, 'slide']):
        count += 1

print('times increased: ', count)
