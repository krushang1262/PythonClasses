import pandas as pd 

# 7) Get information about your Data Frame using info () 

carData = {'car':['Audi','Tata','Bmw','Thar'],'price':[150000,200000,300000,500000],'Qty':[5,4,3,2]}
inf = pd.DataFrame(carData)
print(inf.info())