import pandas as pd 
from sklearn.linear_model import LinearRegression

df = pd.read_csv('~/Desktop/gameAdd/gaming_addiction.csv')

X = df[['Ad_Spend_Lakhs']]
y = df['Daily Order']

model = LinearRegression()
model.fit(X, y)

# Calculate R-squared
r_squared = model.score(X, y)

print("R-squared:", r_squared)