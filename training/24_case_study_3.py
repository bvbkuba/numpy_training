from pandas_datareader.stooq import StooqDailyReader
import pandas as pd
import numpy as np

df = StooqDailyReader(symbols='FB.US').read()
# print(df)

df['Open_group']= pd.cut(x=df['Open'], bins=[80,100,200,df['Open'].max()])
print(df.groupby(['Open_group']).agg({'Open':['sum','mean']}).apply(np.round))
