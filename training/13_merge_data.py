import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.random.rand(5,3), columns=list('abc'))
df2 = pd.DataFrame(np.random.rand(5,3), columns=list('abf'))
df3 = pd.DataFrame(np.random.rand(10,3), columns=list('efg'))
s = pd.Series(np.random.rand(5),name = 'x')


# łączenie dataframe

# df = pd.concat(([df1,df2,df3])) #tak jak # dfx.append(df2)
# df = pd.concat(([df1,df2,df3]),ignore_index=True) # to samo co df = pd.concat(([df1,df2,df3])).reset_index()

# łączenie cd join = inner

# df =pd.concat([df1,df3],axis=1)  #domyślna join = 'outer', dlatego pokazuje NaN

df =pd.concat([df1,df3],axis=1, join='inner') #inner dopasowuje indeksy i pokazuje tylko te, ktore sa takie same w obu df
print(df1,'\n'*2,df3,'\n'*2, df)

dfx = pd.concat([df1,s],axis=1)
print(dfx)


#  append to to samo co concat praktycznie
print(df1.append(df2).reset_index().drop('index',axis=1))
print(df1.append(df2,ignore_index=True))  #tutaj nie musimy uzywać .drop('index',axis=1)


