# 78) Write a python program to find the longest words. 

with open("D:/Python Practice/Assignment/Demo.txt",'r') as f:
    data = f.read().split()
    longest_word = ""
    longest_num = 0
    
    for dt in data:
        if len(dt) > longest_num:
            longest_word = dt
            longest_num = len(dt)
    
    print("longest words:",longest_word)