# 11) Write a Python program to test whether a passed letter is a vowel or not. 

letter = str(input("Enter Letter: ").lower())

if letter in ('a','e','i','o','u'):
    print("It is Vowel")
else:
    print("It is not Vowel")