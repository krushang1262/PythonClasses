import pandas as pd 
import matplotlib.pylab as plt
import seaborn as sbn
import numpy as np

df = pd.read_csv('~/Downloads/ecommerce_transactions.csv')
# df.info()
# df.describe()
# df.head(5)
# df.tail(5)
# df.index
# df.columns
# df.shape

df1 = df.groupby('User_Name')['Transaction_ID'].count().reset_index()
df1 = df1.sort_values(by='Transaction_ID',ascending=False).head(5)
print(df1,'\n')

sbn.barplot(data=df1,x='User_Name',y='Transaction_ID',palette='viridis')
plt.title("Top 5 Users by Number of Transactions")
plt.show()

df2 = df.groupby('User_Name')['Transaction_ID'].count().reset_index()
df2 = df2.sort_values(by='Transaction_ID', ascending=True)
print(df2.head(5),'\n')

df3 = df.groupby('Payment_Method')['Purchase_Amount'].sum()
print(df3,'\n')
plt.pie(df3,labels=df3.index, autopct='%.2f%%')
plt.show()