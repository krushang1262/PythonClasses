# 6) Write a Python program to get the Fibonacci series of given range. 

x=0
y=1

for i in range(25):
    z = x+y
    print(f"{z} fibonacci series")
    x=y
    y=z