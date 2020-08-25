import pandas as pd
import numpy as np
plv_pl = pd.read_csv('../data/plv_merge.csv',index_col=0)
raw_pl = pd.read_csv('../data/raw_merge.csv', index_col=0)


plv = plv_pl.copy()
raw = raw_pl.copy()

plv.columns = ['Open','High','Low', 'Close', 'Volume']
raw.columns = ['Open','High','Low', 'Close', 'Volume']

df = pd.merge(raw,plv,how='inner',left_index=True,right_index=True)  #inner pokazuje tylko te wiersze, ktore maja dopasowanie. Outer pokazywałoby też none
print(df)

df = pd.merge(raw,plv,how='inner',left_index=True,right_index=True,
              suffixes=(' PLV', ' RAV'))  #suffixes - dodawane sa do nazwy kolumn, gdy sa te same nazwy kolumn
print(df)


# dodanie zmiany procentowej
plv['Change'] = plv['Close']/ plv['Close'].shift(1) -1
raw['Change'] = raw['Close']/ raw['Close'].shift(1) -1


 # Dodanie zmiennej logicznej
plv['Flag'] = plv['Change']>0
raw['Flag'] = raw['Change']>0

# zamiana T/F na int
plv['Flag2'] = plv['Flag'].apply(int)
raw['Flag2'] = raw['Flag'].apply(int)
print(plv)

# korelacja
corelation = df.corr()
print(corelation)

d1 = {'date': ['2019-01-01','2019-01-01','2019-01-02','2019-01-02'],
      'id': ['0001','0002','0003','0004'],
      'product_id': ['558','149','050','060']}

d2 = {'date': ['2019-01-01','2019-01-02','2019-01-02','2019-01-03'],
      'id': ['0001','0002','0003','0004'],
      'price': [199,1249,5590,7660]}

left = pd.DataFrame(d1) #robi z dicta obiekt df
right = pd.DataFrame(d2)
print(left,right)


# inner

df_inner = pd.merge(left,right, how='inner',on=['date','id'])
print('\n', df_inner)

#left join -> how = left
df_left = pd.merge(left,right, how='left',on=['date','id'])
print('\n', df_left)

#right join -> how = right
df_right = pd.merge(left,right, how='right',on=['date','id'])
print('\n', df_right)