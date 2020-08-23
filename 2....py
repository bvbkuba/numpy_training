import numpy as np
import pandas as pd
import random

# generating some data
np.random.seed(0)


#np.random.randint(a,b,ilosc_cyfr) -> <a,b)
# uwaga, random.randint ma normalnie 2 argumenty -> przedziały od do. np ma jeszcze ilość cyfr
A = np.random.randint(0,10,20)
print(A)

series = pd.Series(A,name='los')
print(series)

# dtype oznacza jakiego rodzaju są dane
print((pd.Series(A,name='los').dtype))

# iloc służy do wycinania danych
print(series.iloc[0:4])

# index(zwróci jak wyglądają indexy np.(RangeIndex(start=0, stop=20, step=1)) . W przypadku indeksów tekstowych zwróci np. : Index(['adam', 'tomek', 'roman'], dtype='object')
# name(nienazwany będzie None),shape(zwróci tuple z ilością wierszy)
print(series.index,series.name,series.shape)



# Dodawanie/odejmowanie dwóch Series
N = pd.Series(np.random.randn(5))
M = pd.Series(np.random.randn(6))
# N.add(M), N.sub(M)  divide
# wyjątek - dałem specjalnie 5 i 6 i ostatni wiersz się nie dodał, wyszło: nan-> <class 'numpy.float64'>
print(N.add(M).values[-1], type(N.add(M).values[-1]))


# usuwanie duplikatów
np.random.seed(1)
A = np.random.randint(0,5,10)
A = pd.Series(A)
print(A,A.drop_duplicates())

# usuwanie pustych -> .dropna()
A[4] = np.nan
print(A, A.dropna())



