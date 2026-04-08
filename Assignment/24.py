# 24 Write a Python function to insert a string in the middle of a string

def my_middle_string_add_funct():
    text = input("Enter the string: ")
    newtext = "Hello"
    divEqualLen = len(text) // 2
    addedInMiddleOfString = text[:divEqualLen] + " " + newtext +" " + text[divEqualLen:]
    return addedInMiddleOfString

finopt = my_middle_string_add_funct()
print(finopt)