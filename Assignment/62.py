# 62) Write a Python function to check whether a number is in a given range 

def range_function(number):
    
    if number in range(1,25):
        print(f"{number} is in range")
    else:
        print(f"{number} is out of range")
       
range_function(25)