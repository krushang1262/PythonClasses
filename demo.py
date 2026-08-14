import pandas as pd 

df1 = pd.read_csv('~/Desktop/gameAdd/gaming_addiction.csv')
df = pd.DataFrame(df1)
print("strongly positive corelation: ",df["Order_Value"].corr(df["Delivery_Distance"]))
print("strongly positive corelation: ",df["Delivery_Charge"].corr(df["Delivery_Distance"]))
