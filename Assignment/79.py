# 79) Write a Python program to count the number of lines in a text file. 

with open("D:/Python Practice/Assignment/Demo.txt",'r') as f:
    lines = f.readlines()
    count = 0

    for l in lines:
        count +=1
    print(f"total numbers of lines are {count}")