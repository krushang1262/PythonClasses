import pandas as pd

array = [['A','A','A','B','B','B'],[1,2,3,1,2,3]]
array_index = pd.MultiIndex.from_arrays(array, names=("class","Roll no"))
df = pd.DataFrame({"Marks":[10,20,30,40,50,100]},index=array_index)
print(df)

x = df.reset_index()
print(x)
