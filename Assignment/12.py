# 12) Write a Python program to sum of three given integers. However, if two values are equal sum will be zero

n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
n3 = int(input("Enter number 3: "))

sum = 0

if n1 == n2 or n2==n3 or n3 == n1:
    print(f"Two number are same value is: {sum}")
else:
    sum = n1+n2+n3
    print(f"Final all values sum output: {sum}")