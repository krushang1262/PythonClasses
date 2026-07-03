import pandas as pd 

array = [['A','A','A','B','B','B'],[1,2,3,1,2,3]]
arr_index = pd.MultiIndex.from_arrays(array, names=('section-A','marks'))
print(arr_index,'\n')

tuples1 = [('A',1),('A',2),('A',3),('B',1),('B',2),('B',3)]
tup_index = pd.MultiIndex.from_tuples(tuples=tuples1, names=('class','no'))
print(tup_index,'\n')

pro = [['A','B','C','D'],[1,2,3,1,3]]
pro_index = pd.MultiIndex.from_product(pro,names=('c1','n1'))
print(pro_index)