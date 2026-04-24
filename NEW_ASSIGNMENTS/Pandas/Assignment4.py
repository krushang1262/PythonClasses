import pandas as pd 

# 4) Combine the Series of cars and colors into a Data Frame 

carColor = pd.Series(['Red','White','Black'],['Audi','BMW','Tata'])
df = pd.DataFrame(carColor)
print(df)