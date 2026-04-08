# 19) Write a Python program to count the occurrences of each word in a given sentence 
name =  input("Enter name: ")

word = name.split()
for i in word:
    print(f"{i}: {word.count(i)}")