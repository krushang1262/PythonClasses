# Print numbers from N to 1

def my_num(n):
    if n == 0:
        return 1
    print(n)
    my_num(n-1)

my_num(10)

# Print numbers from 1 to N

def num_n(n1):
    if n1 == 0 or n1 <0:
        return 1
    print(n1)
    num_n(n1-1)
    
num_n(5)

# Sum of first N natural numbers

def sum_num(n):
    if n == 0:
        return 0
    return n + sum_num(n-1)
        
print(sum_num(5))

# Factorial of a number

def myfact(n):
    if n == 1:
        return 1
    return n * myfact(n-1)

print(myfact(5))

# Count digits of a number

def count_num(n):
    if n == 0:
        return 0
    return 1 + count_num(n //10)
        
print(count_num(123456789))

# Sum of digits

def sum_dig(n):
    if n == 0:
        return 0
    
    rem = n %10
    return rem + sum_dig(n //10)

print(sum_dig(123))

# Reverse a number

def rev_num(n):
    if n == 0:
        return 0
    
    return int(str(n)[::-1])

print(rev_num(123456))