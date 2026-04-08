print("===========w+=============")

with open("D:/Python Practice/Practice/HandleFile/new.txt","w+") as f:
    x = f.write("Hello Good Morning\n")
    y = f.writelines(["Amazon\n","Flipkart\n","Meesho\n","Snapdeal\n"])
    print(x,y)

print("===========r+=============")

with open("D:/Python Practice/Practice/HandleFile/new.txt","r+") as f:
    y = f.readline(6)
    z = f.readlines()
    print(y,z)

print("===========r+=============")

with open("D:/Python Practice/Practice/HandleFile/new.txt","a+") as f:
    x = f.writelines(["\nMumbai\n","Dharavi\n"])
    print(x)
    y = f.write("\nRadhe most wanted\n")
    print(x,y)

with open("D:/Python Practice/Practice/HandleFile/new.txt","r+") as f:
    f.seek(15)
    d = f.read()
    print(d)