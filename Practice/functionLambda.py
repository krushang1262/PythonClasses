from functools import reduce

# Square of a Number
# Write a lambda function to find the square of a given number.

def lam_func(n):
    sq = lambda n:n*n
    return sq(n)

print(lam_func(34))

# 2. Add Two Numbers
# Write a lambda function that takes two numbers and returns their sum.

def two_num(a,b):
    sm = lambda a,b:a+b
    return sm(a,b)

print(two_num(20,30))

# 3️ Check Even or Odd
# Write a lambda function that checks whether a number is even or odd.

def my_odd_even_func(n):
    res = lambda n: "even" if n%2==0 else "odd"
    return res(n)
print(my_odd_even_func(4))

# 4️ Find Maximum of Two Numbers
# Write a lambda function to find the maximum of two numbers.

def max_num(a,b):
    res = lambda a,b: a if a > b else b
    return res(a,b)
print(max_num(23,245))

# Multiply All Elements in a List
# Write a lambda function with reduce() to multiply all numbers in a list

lst = [45,67,43,21,5]
key = reduce(lambda x,y : x*y, lst)
print(key)

# 6️ Filter Even Numbers
# Using filter() and lambda, write a program to extract even numbers from a list.

evn = [23,12,45,32,31,56,53,78,98,75,43]
k = filter(lambda a:a%2==0,evn)
print(list(k))

# 7️ Square All Numbers in a List
# Using map() and lambda, write a program to square each element of a list.

l = [2,3,4,5,6,7]
k = map(lambda a:a*a,l)
print(list(k))

# 8️ Find Numbers Greater Than 10
# Using filter() and lambda, write a program to get numbers greater than 10 from a list.

l2 = [2,4,5,10,89,34,21,56,15,41]
keys = filter(lambda a:a>10, l2)
print(list(keys))

# Check String Length
# Write a lambda function that checks whether the length of a string is greater than 5.

txt = "Krushang"
kk = lambda a: "yes" if len(a) > 5 else "no"
print(kk(txt))