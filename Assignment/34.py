# 34) Write a Python function that takes two lists and returns true if they
# have at least one common member. 

def my_common_func():
    l1 = [1,2,3,4,5]
    l2 = [4,5,6,7,8]
    
    for i in l1:
        if i in l2:
            return True
    return False

print(my_common_func())