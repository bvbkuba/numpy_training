import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# seaborn. load_dataset moze pryzjmować też inne pliki: https://github.com/mwaskom/seaborn-data
tit = sns.load_dataset('titanic')

# grouping by sex and ploting
by_sex = tit.groupby('sex').size()
print(by_sex)
by_sex_and_survived = tit.groupby(['sex','survived']).size()
print(by_sex_and_survived)

# wyciecie tylko survived dla klasy
print(tit.groupby('class').mean()['survived'])


#data - dane, values - po czym zliczać index - wiersze, aggfunc - func agregujaca np. sumy itp
pivottable = pd.pivot_table(data=tit, values='survived',index='sex',columns='class',aggfunc='count')
print('\n',pivottable)

#robienie przedziałów
tit['age_bin']= pd.cut(x=tit['age'], bins=[0,18,45,tit['age'].max()])
pivot_binage = pd.pivot_table(data = tit, values = 'age',index='age_bin', aggfunc='count')
print(pivot_binage)

# z przedziałami po
pivot_multi = pd.pivot_table(data = tit,index='age_bin',columns='class', aggfunc={'survived':'count','age':'mean'})
print('\n',pivot_multi)