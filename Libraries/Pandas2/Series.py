import pandas as pd

# single table format show records with its index

s1 = pd.Series([1,2,3,4,5])
print(s1)

s2 = pd.Series([1,2,3,4], index=[10,60,30,40])
print(s2)

s3 = pd.Series({1:'a',2:'b',3:'c',4:'d'}, index=[1,2,3,7])
print(s3)

s4 = pd.Series(10, index=[20,30,40,50])
print(s4)