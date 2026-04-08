# 61)Write a Python function to calculate the factorial of a number (a nonnegative integer)

def sum_factorial(number):
    sum =1
    while number !=0:
        sum*=number
        number-=1
    print(sum)
    
sum_factorial(5)        