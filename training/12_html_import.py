import pandas as pd
import numpy as np


# [0] aby pozbyć się [ co stało przed tabela
# columns = ['Otwarcie', 'Najwyzszy', 'Najnizszy', 'Zamkniecie', 'Wolumen']
# headers1 = pd.read_html('../data/small.html',header=0,index_col=0,skiprows=2)[0]
# headers1.columns = columns

# aby pobrać tabele ze strony to podajemy link
nbp = pd.read_html('https://finance.yahoo.com/cryptocurrencies')[0]
print(nbp)
print(nbp.columns)
