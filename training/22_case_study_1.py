import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# #  prepare data
#
# df = pd.read_csv('../data/Consumer_Reviews_Amazon.csv', sep = ',', index_col = 0, nrows=1000)
#
# df.columns = [col.replace('.','_') for col in df.columns]
#
#
# df = df[['name','primaryCategories', 'reviews_rating', 'reviews_text']]
# print(df.describe())
#
# df.to_csv('../data/Review_change.csv')

dfw = pd.read_csv('../data/Review_change.csv')
valcounts = dfw['primaryCategories'].value_counts()
print(valcounts)
# print(valcounts.plot(kind = 'pie', legend = True)) #kołowy wykres
print(dfw.groupby('name').count()['id'])

