import pandas as pd

array = [['A','A','A','B','B','B'],[1,2,3,1,2,3]]
array_index = pd.MultiIndex.from_arrays(array, names=("class","Roll no"))
df = pd.DataFrame({"Marks":[10,20,30,40,50,100]},index=array_index)
print(df,"\n")

tuple = [('A',1), ('A',2), ('A',3), ('B',1),('B',2),('B',3)]
tuple_index = pd.MultiIndex.from_tuples(tuple, names=("class","rollno"))
dft = pd.DataFrame({"Marks":[10,20,30,40,50,60]}, index=tuple_index)
print(dft,"\n")

product = [('A','B'),(10,20)]
product_index = pd.MultiIndex.from_product(product, names=("classes","Roll no"))
df = pd.DataFrame({"Marks":[25,36,14,74]}, index=product_index)
print(df)
