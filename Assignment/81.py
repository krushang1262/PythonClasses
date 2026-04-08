# 81) Write a Python program to write a list to a file.

with open("D:/Python Practice/Assignment/newDemo.txt",'w') as f:
    f.writelines(["hello\n","python\n","java\n","reactjs\n","nodejs\n"])