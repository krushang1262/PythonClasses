import pandas as pd 
import numpy as np

df = pd.read_csv('~/Downloads/zomato_order_dataset.csv')
pop_mean = df['Order Amount'].mean()
pop_median = df['Order Amount'].median()
pop_mode = df['Order Amount'].mode()[0]

print("--- Population Metrics ---")
print(f"Population Mean: {pop_mean}")
print(f"Population Median: {pop_median}")
print(f"Population Mode: {pop_mode}\n")

sample = df['Order Amount'].head(5)
sample_mean = sample.mean()

print("--- Sample Metrics (First 5 Rows) ---")
print(f"Sample Values: {sample.tolist()}")
print(f"Sample Mean: {sample_mean}\n")

diff = abs(pop_mean - sample_mean)
print(diff)