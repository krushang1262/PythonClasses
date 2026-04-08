# 21) Write a Python program to add 'in' at the end of a given string (length
# should be at least 3). If the given string already ends with 'ing' then 
# add 'ly' instead if the string length of the given string is less than 3, leave it unchanged.

text = str(input("Enter the string: "))
txt = len(text)


if txt !=0:
    if txt < 3:
        print(text)
    elif text.endswith("ing"):
        print(text[0:]+"ly")
    elif text.endswith !=("ing"):
        print(text[0:]+"in")
else:
    print("string is empty. pla entered the string  ")
















