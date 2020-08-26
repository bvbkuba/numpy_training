import pandas as pd
import numpy as np

retail = pd.read_excel('../data/Online_retail.xlsx')
print(retail.info())
print(retail.head())  #domyślnie 5 pierwszych wierszy
print(retail.tail(2))  # 2 ost. wiersze

retail = retail[retail['CustomerID'].notnull()]  #maska logiczna =- pokaze tylko wartosci true
retail['CustomerID'] = retail['CustomerID'].apply(lambda x:str(int(x))) #konwertowanie na str
retail['StockCode'] = retail['StockCode'].apply(lambda x:str(x))
# print(retail.groupby('CustomerID').size())
print(retail.head())

# retail['Quantitybool'] = retail['Quantity'] >0  #sprawdzenie ile jest dodatnich a ile ujemnych
# print(retail.groupby('Quantitybool').size())

retail = retail[retail['Quantity']>0]
# print(retail.info())


"""SELECT Quantity,UnitPrice
FROM Retail"""

query = retail[['Quantity','UnitPrice']]
print(query)

"""SELECT Quantity,UnitPrice
FROM Retail
LIMIT 10"""

query = retail[['Quantity','UnitPrice']][:10]
print(query)

"""SELECT * 
FROM Retail
WHERE
StockCode = '71053'"""


query = retail[retail['StockCode']=='71053']

retail['x'] = pd.api.types.is_string_dtype(retail['StockCode'])
success = retail.groupby('x').size()
print('\n',f'Success;{success}','\n')
print(retail)

print('\n',retail['CustomerID'].dtype.kind)


"""Select * from retail 
where CID = 17850 and StockCode = 85123A"""
print(retail[(retail['CustomerID']== '17850') & (retail['StockCode']=='85123A')])
print(retail.query("""CustomerID == '17850' and StockCode == '85123A'"""))


"""Select * from retail 
where invoicesno is not null"""
print(retail[retail['InvoiceNo'].notnull()])

"""select customerid, avg(revenue),count(*)
from retail
group by customerid"""

result = retail.groupby('CustomerID')\
    .agg({'Quantity': np.mean, 'CustomerID':np.size})\
    .rename(columns={'Quantity':'Avg_quantity'})
print(result)


#wyciaganie dnia z daty
print(retail['InvoiceDate'].dt.day)

#najlepsze 5 wartości quantity
query = retail[['Quantity','StockCode']]
print(query)
query = query.nlargest(5,'Quantity')
query = query.sort_values('Quantity',ascending=True)
print('\n','pppp',query)