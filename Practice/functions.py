# 1. Find Maximum of Two Numbers
# Write a function that takes two numbers and returns the greater number.

def greater_num(a,b):
    if a > b:
        return a
    else:
        return b
print(greater_num(6,7))

# 2. Check Even or Odd
# Write a function that accepts a number and returns whether it is even or odd.

def odd_evenfunc(num):
    if num%2==0:
        print("Even")
    else:
        print("Odd")
odd_evenfunc(90)

# 3. Reverse a String
# Write a function that takes a string and returns the reversed string.

def rev_str(n):
    print(n[::-1])
rev_str("Krushang")

# 4. Count Vowels in a String
# Write a function that counts how many vowels (a, e, i, o, u) are present in a given string.

def count_vowel(c):
    if 'a' in c or 'e' in c or 'i' in c or 'o' in c:
        print("Vowel")
    else:
        print("not vowel")
        
count_vowel("o")

# 5. Factorial of a Number
# Write a function that returns the factorial of a given number.

def my_fact(n):
    fact = 1
    for i in range(fact, n+1):
        fact*=i
    return fact

print(my_fact(5))

def my_fact2(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * my_fact2(n-1)

t = my_fact2(5)
print(t)

# 6. Check Palindrome
# Write a function that checks whether a given string or number is a palindrome.

def my_palindrome(txt):
    t3 = txt[::-1]
    
    if txt == t3:
        print("Palindrome")
    else:
        print("Not palindrome")
my_palindrome("radar")

# 7. Find Sum of List Elements
# Write a function that takes a list of numbers and returns the sum of all elements.

def sumof_func(ls):
    x = 0
    for l in ls:
        x = x+l
    return x

print(sumof_func([2,3,43,58,69,71,18,9]))

# 8. Find Second Largest Number in a List
# Write a function that finds the second largest number from a list.

def sec_largest_num():
    
    lss = [45,67,89,32,23,45]
    old_val = min(lss)
    lss.remove(old_val)
    
    aga_min_val = min(lss)
    print(aga_min_val)
    
sec_largest_num()
    
# 9. Check Prime Number
# Write a function that checks whether a given number is prime or not.

def my_prime(n):
    if n%2==0:
        print("Prime")
    else:
        print("not prime")
my_prime(30)

# 10. Count Occurrence of Each Character
# Write a function that takes a string and returns the frequency of each character.

def count_freq(st):
    for s in st:
        print(f"{s} : {st.count(s)}")

count_freq("radaar")