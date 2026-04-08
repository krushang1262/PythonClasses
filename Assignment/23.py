# Write a Python program to get a string made of the first 2 and the last
# 2 chars from a given a string. If the string length is less than 2, return
# instead of the empty string

text = "Krushang"
text1 = ''
if len(text) < 2:
    print("")
else:
    text1 = text[:2] + text[-2:]
print(text1)