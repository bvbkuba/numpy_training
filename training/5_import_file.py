import pandas as pd
import numpy as np


#import z csv
# index_col = 0 -> data bedzie indeksem a nia ciag cyfr
#skiprows = zacznij od x+1, nrows = weź x wierszów
df = pd.read_csv('../data/cdr_d.csv',index_col=0,skiprows=6000,nrows=10)
df = pd.read_csv('../data/cdr_d.csv',index_col=0,nrows=10)


# export to csv
df = pd.read_csv('../data/cdr_d.csv', nrows=20, index_col=0)
closest_price = df['Zamkniecie']
closest_price.to_csv('../data/close_price.csv', header=['close'])  #jak plik csv nie istnieje to py go stworzy

# export to json
closest_price.to_json(('../data/close.json'))  # stwoorzy plik jak nie istnieje

# eksportowanie do słownika
x = closest_price.to_dict()
print(x)

# importowanie danych ze schowka
df_clipboard = pd.read_clipboard()
print(df_clipboard)
# df.to_clipboard()
df_clipboard.to_csv('../data/file_from_clipboard.csv')

