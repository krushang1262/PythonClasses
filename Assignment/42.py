# 42) Write a Python program to split a list into different variables. 
x = [1,2,3,4,5,6,7]
a, b, c, *rest = x

print(a)
print(b)
print(c)
print(rest)