# 20) Write a Python program to get a single string from two given strings, 
# separated by a space and swap the first two characters of each string

text = "Python for data analysis"
text2 = "powerBi excel for d.a"

swap1 = text[:2] + text2[2:]
swap2 = text2[:2] + text[2:]

result = swap1 +" "+ swap2

print(result)