import pandas as pd 

# 6) Describe your current car sales Data Frame using describe ()

carData = {'car':['Audi','Tata','Bmw','Thar'],'price':[150000,200000,300000,500000],'Qty':[5,4,3,2]}

desc = pd.DataFrame(carData)
desc['currentSales'] = desc['price'] * desc['Qty']

print(desc.describe())