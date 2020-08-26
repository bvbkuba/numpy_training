import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('https://raw.githubusercontent.com/krakowiakpawel9/pandas_course/master/15_case_study_google/data/googleplaystore.csv')
# print(df)

# preprocessing
print(df.info(), df.describe())  #describe podaje sumy,srednie itp. info to info
df.columns = [col.replace(' ', '_') for col in df.columns]
print(df.columns)

#  udelete bad row and calculate index again
df = df.drop(10472)
df = df.reset_index()

# check is numeric
print(pd.api.types.is_numeric_dtype(df.Reviews))

df.Reviews = pd.to_numeric(df.Reviews)

tmp = df.groupby('Category').size().rename('Count')
print(tmp, '\n'*2)

tmp2 = df.groupby(['Category','Rating']).agg({'Rating': ['count', 'mean']})
print(tmp2)