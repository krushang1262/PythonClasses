# 77) Write a Python program to read a file line by line store it into a variable.

with open("D:/Python Practice/Assignment/Demo.txt",'r') as f:
    for data in f:
        line = data
        print(line)