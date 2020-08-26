import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pytz
from pandas_datareader import DataReader

# szeregi czasowe

# rng = pd.date_range('2020-10-10', periods=10,freq='Q')
# print(rng)

# freq może być H,S,T-Minutes, Q, W-weekly, D- calendar day, B - business day,
# M- Month end MS - month start, A- year end



# Time zone

# time_zones = list(pytz.all_timezones)
# europe_timezones = [tz for tz in time_zones if tz.startswith('Europe')]
# print(europe_timezones)

# zmiana timezone - th_convert(tz= strefa czasowa)

#data reader pobiera dane z internetu
amazon = DataReader('AMZN','stooq')
amazon.to_csv('../data/amazon_datareader.csv')


# skumulowane wykresy za pomocą subplots (3 to ilość rodzaji ax=ax[x]
# amazon = amazon.sort_index()
fig,ax = plt.subplots(3, sharex = True)
amazon['Close'].plot(ax = ax[0])
amazon['Close'].rolling(120).mean().plot(ax = ax[1],logy = True)  #logy = logarytmiczny
amazon['Close'].plot(ax = ax[1])
amazon['Close'].plot(ax = ax[2])
ax[0].legend(['price','rolling'])
ax[1].legend(['price'])
ax[2].legend(['test'])