import pandas as pd

# 16) Use. iloc to select the row at position 3 of the car sales Data Frame

carData = {'car':['Audi','Tata','Bmw','Thar','Benz','RangeRover','Inovva','Creta'],
           'price':[150000,200000,300000,500000,600000,700000,590000,630000],
           'Qty':[5,4,3,2,4,3,2,6]}

df = pd.DataFrame(carData)

x = df.iloc[3]
print(x)