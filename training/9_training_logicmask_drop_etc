import numpy as np
import pandas as pd

df = pd.read_csv('../data/aapl_us_d.csv',index_col=0,nrows=10)
df.columns=['Open','High','Low','Close','Volume']


# maska logiczna - daje wartosci nan, gdzie warunek df>100 nie jest spełniony
df_ = df[df > 100]
print(df_)
print(df.query('Close <0.42'))

print('*' *100)

# Szeregi czasowe
date = pd.date_range('01-10-2019', periods=10)
print(date)

# aby robić +-*/ na Df to muszą być te same kolumny i dokładnie taka sama tabels
df1 = pd.DataFrame(np.random.randn(10,3), columns=list('ABC'))
df2 = pd.DataFrame(np.random.randn(10,3), columns=list('ABC'))
print(df1+df2)

# sample(n) - wartości losowe
print(df.sample(3))

# frac - oznacza ile % wierszy zwrócić
print(df.sample(frac= 0.25))

# usuwanie duplikatow
funny_lottery = pd.DataFrame(np.random.randint(0,10,20))
print(funny_lottery.drop_duplicates())

# drop na kolumnach
delete_col = df.drop(['Open','High'],axis=1)
print(delete_col)

# tu nie zadziała bo nie mam pliku, ale sam schemat jest zrozumiały

# convert_numbers = df['Volume'].apply(lambda s: s.replace(' ', ''))
# print(convert_numbers)

# df loc - operacje na datach
print(df.loc['1984-09-15':])
