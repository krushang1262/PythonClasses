import pandas as pd

array = [['A','A','A','B','B','B'],[1,2,3,1,2,3]]
abc_index = pd.MultiIndex.from_arrays(array, names=("class","Roll no"))

df = pd.DataFrame({"Marks":[10,20,30,40,50,60]}, index=abc_index)
print(df)
x= df.droplevel("class")
print(x)