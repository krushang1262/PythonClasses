import json

try:
    nm = input("Enter name: ")
    email = input("Enter email: ")
    age = int(input("Enter age: "))

    d = {"name":nm, "email":email,"age":age}

    with open("D:/Python Practice/Practice/HandleFile/js.json","w+") as f:
        json.dump(d,f)
        
except Exception as e:
    print(e)

finally:
    print("finally part is execute")