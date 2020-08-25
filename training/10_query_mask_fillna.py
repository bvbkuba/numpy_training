import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(20,5),columns=list('abcde'),index=list('abcdefghijklmnoprstu'))
print(df)

# w df zamiast and dajemy &   ->
mask = (df.a >0) & (df.c > 0)
print(mask)  # zwraca T or F dla wierszy
and_conditional = df[mask]  #nakładamy maskę czyli tam gdzie jest True w warunkach to pokaze wartosci
and_conditional =  df[(df.a >0) & (df.c > 0)]  #ten sam zapis out
print(and_conditional)

# or = |
or_conditional = df[(df.a >0) | (df.c > 0)]
print(or_conditional)



# operator where   -> zwróci Nan tam gdzie jest warunek niespełniony
where_cond = df.where(df.a>0)    #0 po przecinku oznacza daj 0 tam gdzie ma byc Nan
print(where_cond)

# query - zapytania z sql, łaczenie poprzez & i |
queryy = df.query('(a>0) & (b<0)')
print('Query to :',queryy)



# zaokraglanie wartosci
print(df.round(2))

# filtrowanie brakujacych wartosci
df = pd.DataFrame(np.random.rand(10,4),columns=['one','two','three','four'])
print(df)

for row in df.values:
    switch = np.random.choice([0,1])
    if switch:   #czyli =1
        i = np.random.choice([0,1,2,3])
        row[i] = np.nan

print(df, df.isnull())

print('*'*50)
# tutaj pokaże wszystkie kolumny gdzie kolumna one ma wartości null
print(df[df['one'].isnull()])

#  tylda oznacza negacja czyli da wszystkie tam gdzie one != 1
print(df[~df['one'].isnull()])  #czyli to samo co df[df['one'].notnull()]

# usuwanie kolumny
del df['two']
print(df)

# wypełnienie jednej kolumny
df['one'] = df['one'].fillna(200)
print(df)

# wypełnienie Nan średnią dla danej kolumny
print(df.fillna(df.mean()),df.mean())

df = pd.DataFrame(np.random.randn(20,5),columns=list('abcde'),index=list('abcdefghijklmnoprstu'))
print(df)

for row in df.values:
    switch = np.random.choice([0,1])
    if switch:   #czyli =1
        i = np.random.choice([0,1,2,3])
        row[i] = np.nan

print(df)
df2  =  df.dropna(axis=0)   #pokaze tylko wiersze, ktore nie maja Nan
df3 = df.dropna(axis=1)   #pokaze tylko kolumny ktore nie maja Nan
print(df2,'\n'*2,df3)