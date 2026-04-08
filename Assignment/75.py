# 75) Write a Python program to read last n lines of a file. 

n = int(input("Enter the line no: "))
with open("D:/Python Practice/Assignment/Demo.txt",'r') as f:
    data = f.readlines()
    for d in data[-n:]:
        print(d)