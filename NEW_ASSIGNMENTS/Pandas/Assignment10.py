import pandas as pd 

# 10) List out all the column names of the car sales Data Frame 

carData = {'car':['Audi','Tata','Bmw','Thar'],'price':[150000,200000,300000,500000],'Qty':[5,4,3,2]}
ls = pd.DataFrame(carData)
print(ls.columns)