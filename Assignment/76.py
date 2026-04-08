# 76) Write a Python program to read a file line by line and store it into a list
newList = []
 
with open("D:/Python Practice/Assignment/Demo.txt",'r') as f:
    for line in f:
        newList.append(line.strip())
print(newList)