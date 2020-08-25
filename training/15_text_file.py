import numpy as np
import pandas as pd

s = pd.Series(['   Apple','Microsoft    ',np.nan, 'Google', 'Amazon'], name='Stock')
print(s.str.strip())
print(s.str.upper())
print(s.str.strip())
join_text = s.str.cat(sep = ',')
print(join_text)

c = pd.Series(['#kill#join#fun', '#me#2#you','#he#is#we'])
c1 = c.str.split('#')
c2 = c.str.split('#',expand = True) #rozbija liste i dodaje do kolumn
print(c1,c2,'\n'*2)

c3 = c.str.split('#',expand = True).drop(0,axis=1)#drop(0) -> usuwa 1 wiersz. dodajac axis = 1 usunie kolumne
print(c3)

# cointains służy do regexa, musi mieć r'
string = 'Ala ma kota. Ala dba o niego i jest z siebie dumna. To Ala'
sstring = string.split()
s = pd.Series(sstring)
logic_s = s.str.contains(r'[c-d]')
logic_mask = s[logic_s] #'maska logiczna'
print('\n',logic_mask)