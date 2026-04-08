# 80) Write a Python program to count the frequency of words in a file

with open("D:/Python Practice/Assignment/Demo.txt",'r') as f:
    data = f.read().split()
    
    for dt in data:
        print(f"{dt} : {data.count(dt)}")