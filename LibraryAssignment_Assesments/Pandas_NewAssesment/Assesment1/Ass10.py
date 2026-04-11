import pandas as pd
import seaborn as sbn
import matplotlib.pyplot as plt

# Are there outliers in GDP, Gold, or Oil prices?

df = pd.read_csv('~/Desktop/AssignmentData/finance_economics_dataset.csv')
sbn.boxplot(data=df['GDP Growth (%)'])
plt.show()

sbn.boxplot(data=df['Gold Price (USD per Ounce)'])
plt.show()

sbn.boxplot(data=df['Crude Oil Price (USD per Barrel)'])
plt.show()