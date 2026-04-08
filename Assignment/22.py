# 22 Write a Python function to reverses a string if its length is a multiple of 4. 

def my_func_rev():
    text = input("Enter a string: ")
    
    if len(text) % 4 ==0:
        return text[::-1]
    else:
        print(text)

rev = my_func_rev()
print(rev)