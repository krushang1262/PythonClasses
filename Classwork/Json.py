import json

name = input("Enter name: ")
email = input("Enter email: ")

d = {"name":name, "email":email}

with open("D:/Python Practice/Classwork/FileHandaling/J.Json","w+") as f:
    json.dump(d,f)