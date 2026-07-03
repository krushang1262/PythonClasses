import pandas as pd 

df = pd.read_csv('~/Desktop/DataSheet/SampleSuperstore.csv',encoding='latin')
df1 = df.groupby(['Category','Sub-Category'])['Sales'].sum()
# print(df1)

df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Months (Order Date)"] = df["Order Date"].dt.strftime("%b")

df['Years (Order Date)'] = df["Order Date"].dt.year

df2 = df[['Months (Order Date)','Years (Order Date)','Sales']]
df3 = df2.pivot_table(columns='Years (Order Date)',index='Months (Order Date)', values='Sales',aggfunc='sum')
print(df3)