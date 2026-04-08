# 63) Write a Python function to check whether a number is perfect or not

def perf_num(number):
    divisor = sum([num for num in range(1,number) if number % num == 0])
    
    if number == divisor:
        print(f"{number} is perfect number")
    else:
        print(f"{number} is not perfect number")
    
perf_num(6)