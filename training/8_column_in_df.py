import numpy as np
import pandas as pd

df = pd.read_csv('../data/aapl_us_d.csv',index_col=0,nrows=10)
df.columns=['Open','High','Low','Close','Volume']


price_open = df['Open']
price_open2 = df.iloc[:5,:2]  # [wiersze,kolumny]
print(df.Low)
print(df.iloc[:3,[0,3]])
print(df.iloc[::3,[0,2]]) # co trzeci wiersz

df['Average'] = df['Open'] + df['Close']
print(df)

df = df.assign(Trueorfalse=df['Open']>=0)
print(df['Trueorfalse'].aggregate(sum))   # ilość dni >0\

# uwaga - count musi byc w cudzyslowiach, sum może ale nie musi
print(df['Average'].aggregate(sum) / df['Average'].aggregate('count'))
