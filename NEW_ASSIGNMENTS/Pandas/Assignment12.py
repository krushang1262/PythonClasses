import pandas as pd 
# 12) Show the first 5 rows of the car sales Data Frame 

carData = {'car':['Audi','Tata','Bmw','Thar','Benz','RangeRover'],'price':[150000,200000,300000,500000,600000,700000],'Qty':[5,4,3,2,4,3]}
df = pd.DataFrame(carData).head(5)
print(df)