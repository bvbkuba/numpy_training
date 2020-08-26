import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# sns.set()

df = pd.read_csv('../data/raw_merge.csv',index_col=0)
df.columns = ['Open','High','Low', 'Close', 'Volume']
clean_price = df[['Open', 'High','Low','Close']]
volume = df['Volume']

# skumulowany volumen
cum_vol = volume.cumsum()
# cum_vol.plot()

# praca na cenie zamkniecia
close  = df['Close']
# rolling(window = liczba okienek) -> 30 okresowa średnia
close_roll_avg = close.rolling(window= 30).mean()
print(close_roll_avg)

# skumulowany wykres okresowy
close.plot(style = 'k--')
for i in [5,10,30,60,90,120]:
    close_roll_avg = close.rolling(window=i).mean()
    close_roll_avg.plot()  #można od razu plot dać po mean

