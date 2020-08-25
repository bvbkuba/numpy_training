import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# chart basic - one line
ts = pd.Series(np.random.randn(100),index=pd.date_range('2020-10-10',periods=100))
print(ts)

ts = ts.cumsum()
ts.plot()

# more lines in charts

df = pd.DataFrame(np.random.randn(100,3), index=pd.date_range('2020-10-10',periods=100),columns=list('abc'))
print(df)
df = df.cumsum()  #robi sume narastajaco, cummin -> pokazuje najmniejsza napotkana wartos, cummax -max napotkana

abs(df.iloc[6]).plot(kind = 'bar')  #wykres słupkowy
df.plot(kind = 'hist', bins = 40) #histogram lub df.plot.hist(bins = 40)