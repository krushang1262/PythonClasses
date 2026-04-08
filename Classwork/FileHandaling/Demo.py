# f = open("D:/Python Practice/Classwork/FileHandaling/test.txt","w")
# f.write("Hello DataAnalyst\n")
# f.writelines(["Hello World\n","Hello Data\n","Hello Tops\n","Anything\n","something\n"])
# f.close()

f = open("D:/Python Practice/Classwork/FileHandaling/test.txt","r")

while True:
    data = f.readline()
    if "Hello" in data:
        print(data)
    if not data:
        break
f.close()
        
f = open("D:/Python Practice/Classwork/FileHandaling/test.txt","r")

while True:
    data = f.readline()
    # print(data)
    if not data:
        break
    print(len(data))
f.close()

with open("D:/Python Practice/Classwork/FileHandaling/test.txt") as f :
    f.seek(10)
    print(f.tell())
    data = f.read()
    print(f.tell())
    print(data)
