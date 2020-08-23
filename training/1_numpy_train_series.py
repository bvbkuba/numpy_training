import pandas as pd
import numpy as np

s = pd.Series(4)

#Series oznacza, coś w stylu kolumny w Excelu. Wynik s2 =
"""adam     2
    tomek    3
    roman    4
Name: age, dtype: int64
"""
s2 = pd.Series(data = [2,3,4], index=['adam','tomek','roman'],name='age')
#%%
print(s2)

A = np.random.randn(5)  #10 zmiennych typu float z rozkładu normalnego(czyli od 0 max o 3 odch.standardowe w lewo i prawo,
#źródło: https://pogotowiestatystyczne.pl/slowniczek/rozklad-normalny/
print(A)


# tworzenie ze słownika obiektu series - stworzy 2 kolumny: key, value
stocks = {'Apple':'USA', 'CD':'Pol','AMZN':'Py'}
series = pd.Series(stocks,name='Panda')
print(series)

# zamiana obiektu Series/d.frame na tablicę numpy
series2 = series.values
print(series2)   # wtedy są tylko same wartości

aple_series = series['Apple'] #działa tak jak słownik, zwraca string
print(aple_series)

print('Apple' in series, 'USA' in series)  #patrzy tylko na indexy

np.random.seed(0) # powoduje zatrzymanie się randomów
A = np.random.randn(20)
s = pd.Series(A)   # stworzy tabele z indexami od 0-19 i tabele z wartosciami randn
print(s[0])