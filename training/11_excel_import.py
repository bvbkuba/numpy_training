import pandas as pd
import numpy as np

df = pd.read_excel('../data/companies.xlsx',nrows=10)
print(df)

# na_values odpowiada co ma być wartością nan
df = df = pd.read_excel('../data/companies.xlsx',na_values='?',nrows=10, index_col=0)
print(df)


# sheer_name - nazwa arkuszu
df = df = pd.read_excel('../data/companies.xlsx',na_values='?',nrows=10, index_col=0,sheet_name='microsoft')
print(df)

