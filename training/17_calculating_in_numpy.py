import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('../data/raw_merge.csv',index_col=0,nrows=20)
df.columns = ['Open','High','Low', 'Close', 'Volume']
ranks = df.copy()
df['daily_change'] = df['Close'].pct_change()
df['5_days_pctcgOpen'] = df['Open'].pct_change(periods=5) #zmiana pct w porównaniu sprzed 5 dni
print(df)
df['Cols per cols'] =  df[['Open','Close']].pct_change(axis=1).drop('Open',axis=1) #porównuje do poprzedniej kolumny. drop usunie kolumne Nan z podanej nazwy kolumny
print(df)


clean_columns = df[['Open','Close','Cols per cols']] #pokaze df z 3 kolumn
print(clean_columns)

# korelacja
cor_basic= clean_columns.corr()

# korelacja kolumna od kolumny
correlation = clean_columns['Open'].corr(clean_columns['Close'])
print(correlation)

# wykres korelacji
plt.matshow(cor_basic)


# ranking
ranks['Volume_rank'] = ranks['Volume'].rank()  #przyjmuje tez parametr ascending
print(ranks)

# sortowanie
ranks_sort = ranks.sort_values(by= 'Volume_rank')
print(ranks_sort)

# wybieranie topów
top_5 = df.nlargest(n=3,columns='Volume')
print(top_5)

