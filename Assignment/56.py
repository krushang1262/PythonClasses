# 56) Write a Python program to map two lists into a dictionary

from collections import Counter

l1 =['a','b','c','d']
l2 = [400,400,300,400]

x = Counter(dict(zip(l1,l2)))
print(x)