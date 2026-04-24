import pandas as pd 

# 5) Find the different datatypes of the car data Data Frame 

carData = {'car':['Audi','Tata','Bmw','Thar'],'price':[150000,200000,300000,500000],'mileage':[14.54,56.85,78.23,65.21]}
df = pd.DataFrame(carData)
print(df.dtypes)