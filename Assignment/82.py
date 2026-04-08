# 82)Write a Python program to copy the contents of a file to another file. 

with open("D:/Python Practice/Assignment/Demo.txt",'r') as f:
    with open("D:/Python Practice/Assignment/copyContent.txt","w") as cp:
       cp.writelines(f.readlines())