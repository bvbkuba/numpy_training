import numpy as np
import pandas as pd

list_of_capitals = ['Ud','Uda','CCC','simple path','joined', 'neighbour sc','pathing date']
capitals = pd.Series(list_of_capitals, name='CAP')
capitals = capitals.apply(lambda c: c.upper())
print(capitals)
print(capitals.isin(['UD']))   #sprawdza czy jakaś stolica jest 'UD' -> zwraca dla niej True. Jak jest 'UDA' to zwróci False


# tworzenie obiektu data_frame
df = pd.DataFrame([[1,2,3],[3,33,30],[333,2,1]],index=['first','second','third'],columns=['col1','col2','col3'])
print(df)


# df ze słownika - zwróc uwagę na 3,4 wiersz - skoro 2 pierwsze były df, to też tak się przyjął
df_of_dict = {'one': pd.Series([1,2,3]),
     'two':pd.Series([33,332,123]),
    'three': ['a','b','c'],
    'thre': ['a','b','c']}
print(pd.DataFrame(df_of_dict))
