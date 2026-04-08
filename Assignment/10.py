# 10) Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user. 

num = int(input("Enter the number to check it is odd or Even: "))

if num%2==0:
    print(f"Number is Even {num}")
else:
    print(f"Number id odd {num}")