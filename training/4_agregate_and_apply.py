import pandas as pd
import numpy as np

np.random.seed(0)
s = pd.Series(np.random.randn(10))


# agregate tak jakby nic nam nie robi w pojedyńczej wartości , bo py ma wbudowane funkcje ktore dzialaja
minimum = s.min()
print(s.min(), s.aggregate(min),s.aggregate(sum), s.sum(), s.mean(), s.aggregate(np.mean), s.std(), s.aggregate(np.std))
# świetne zastosowanie ma natomiast do tworzenia tabeli, gdzie użyjemy do idx funkcji

print(s.aggregate(['min','max','std']))


# metoda apply(funkcja)

print(s.apply(abs))   #wartość bezwzgl.
print(s.apply(float.is_integer))  #spr czy float to int
print(s.apply(int))  # zamienia na int

print(s.apply(lambda x:100*x))
print(s.apply(lambda b:abs(b)))

# standaryzacja z użyciem aplly - standaryzacja: (x-avg(x))/odch.st.
print(s.apply(lambda x:(x-np.mean(s))/np.std(s)))

# apply z uzyciem wlasnej funkcji
def more_complex(x):
    return x**(0.5)

s.apply(more_complex)
