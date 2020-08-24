import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(20,5),columns=list('abcde'),index=list('abcdefghijklmnoprstu'))
print(df)

for row in df.values:
    switch = np.random.choice([0,1])
    if switch:   #czyli =1
        i = np.random.choice([0,1,2,3])
        row[i] = np.nan

print(df)
df2  =  df.dropna(axis=0)   #pokaze tylko wiersze, ktore nie maja Nan
df3 = df.dropna(axis=1)   #pokaze tylko kolumny ktore nie maja Nan
print(df2,'\n'*2,df3)