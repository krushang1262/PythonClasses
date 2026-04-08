from functools import reduce 
lst =[12,34,56,54,78,98,76,41]

k = reduce(lambda a,b: a if a > b else b ,lst)
print(k)
l = reduce(lambda a,b: a+b,lst)
print(l)