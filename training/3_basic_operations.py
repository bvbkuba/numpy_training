import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# idxmin/max gdy jest w values typ nan to go zwraca jako min/max przy ustawieniu Skipna=False. W przypadku braku nan to zwraca ofc min/max index

A = pd.Series(np.random.randint(3,10,10))
print(A)

A[2] = np.nan
print(A.idxmax())
print(A.idxmin(skipna=False))

# count - zlicza ilośc indeksów, które mają jakieś wartości (nan to nie wartość oczywiście)
print(A.count())

# cumsum zwraca sumy narastająco -> jak jest Nan to zwraca sumę jako Nan, ale w kolejnym idx traktuje go juz jako 0 i sume pozostalych cyfr
print(A.cumsum())
# print(A.cummin()) #cummin zwraca min max dla indeksow
print(A.value_counts(sort=True))


# sum -> sumuje, std - odchylenie standardowe, mean - średnia, describe - złożony opis z count,mean,std,min,percentyle,max
print(A.sum(),A.std(),A.mean(),A.describe())
# print(A.describe()['mean'])



# histogram - najlepiej uruchamiać w konsoli - pokaze wtedy dodatkowo wykres

hist_data = pd.Series(np.random.rand(1000))
hist_data.hist(bins=80,color = 'red')

# wybieranie wartości top i najgorszych
print(A.nsmallest(3),A.nlargest(3))

# kwartyle
print('mediana: ',A.quantile(0.5))
print('1/4: ',A.quantile(0.25))

# zaokrąglanie, bez x -> da int
rounds = pd.Series(np.random.randn(10))
print(rounds.round(2))

# przesuwa o 2 nasze wartości, dając na idx 0,1 wartości nan. Uwaga -> usuwa on wtedy ostatnie 2 wartości aby dodać do listy
y = rounds.shift(2)

# fillna -> służy do tego, aby w miejsce nan dać cyfry
print(y.fillna(5))

# sort_values() -> sortuje rosnąco, indexy są wtedy pomieszane
print(y.sort_values(ascending=False))


# liczba eulera-2,73 do potęgi
print(np.exp(2))
