# 45) Write a Python program to unzip a list of tuples into individual lists. 4

lst = [(1,'a'),(2,'b'),(3,'c'),(4,'d'),(5,'e')]

k = zip(*lst)
print(list(k))