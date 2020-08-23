import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = '../data/cdr_d.csv'
df = pd.read_csv(path)
close = df['Zamkniecie']
close = close[1:10] # po indeksach bo nie określilismy index_col
print(close)

df = pd.read_csv(path,index_col=0)
volumen = df['Wolumen']
volumen = volumen['2010-01-01': '2010-02-10']  #zakres dat



# Aby wyswietlil sie wykres, musimy to wpisywac w consoli pythona
volumen.plot()
volumen.plot(title = 'Charts of volumens', logy= True)

# zapis wykresu - dzieki matplotlib
plt.savefig('../charts/charts_of_vol_p_6')  #opcjonalnie ma parametr format

