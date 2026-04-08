# 64)Write a Python function that checks whether a passed string is palindrome or not 

def str_palindrome(s):
    
    if s[0::] == s[::-1]:
        print("string is palindrome")
    else:
        print("string is not palindrome")
        
str_palindrome("radar")