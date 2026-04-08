# print("===============write==================")

f = open("D:/Python Practice/Practice/HandleFile/demo.txt","w")
data = f.write("Hello these is my new Files")
print(data)
f.close()

# print("===============read==================")

f = open("D:/Python Practice/Practice/HandleFile/demo.txt","r")

data = f.read() # read whole file
print(data)

data1 = f.readline(5) # read the file for given through number 
print(data1)

data2 = f.readlines() # give all content in the list then after display in list 
print(data2)

print("===============append==================")

f = open("D:/Python Practice/Practice/HandleFile/demo.txt","a")
data = f.write("\nHello DataAnalyst")
print(data)

data2 = f.writelines(["\nHello Python","\nHello Java","\nHello ReactJs","\nHello NodeJs"])
print(data2)

print("===============with==================")

with open("D:/Python Practice/Practice/HandleFile/demo.txt") as f:
    data = f.read()
    print(data)
    
    d1 = f.readline(3)
    print(d1)
    
    d2 = f.readlines()
    print(d2)

with open("D:/Python Practice/Practice/HandleFile/withDemo.txt","w") as f:
    data = f.write("Good Morning")
    print(data)
    
    data = f.writelines(["\nDataScience","\nMachineLearning","\nGenerativeAI"])
    print(data)

with open("D:/Python Practice/Practice/HandleFile/withDemo.txt","r") as f:
    d = f.read()
    print(d)
    
    d1 = f.readline(5)
    print(d1)
    
    d2 = f.readlines()
    print(d2)

with open("D:/Python Practice/Practice/HandleFile/withDemo.txt","a")as f:
    d = f.write("\nApple\n")
    print(d)
    
    d1 = f.writelines(["\nSamsung","\nAcer","\nIntel","\nVivo","\nNokia"])
    print(d1)

with open("D:/Python Practice/Practice/HandleFile/withDemo.txt","r")as f:
    f.seek(7)
    d = f.read()
    print(d)
    print(f.tell())
    