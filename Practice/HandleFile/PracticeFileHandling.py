# Count characters in a file

with open("D:/Python Practice/Practice/HandleFile/Practice.txt","r") as f:
       data = f.read()
       print("total character:",len(data))
       
# Count words and lines in a file

with open("D:/Python Practice/Practice/HandleFile/Practice.txt","r") as f:
       data = f.read()
       print("total words",len(data.split()))      
       print("total lines",len(data.splitlines()))      

# Read first 10 characters of a file

with open("D:/Python Practice/Practice/HandleFile/Practice.txt","r") as f:
       print(f.tell())
       print(f.read(10))
       print(f.tell())

# Read a file and print only even lines

with open("D:/Python Practice/Practice/HandleFile/number.txt","r") as f:
       data = f.readlines()
       
       for i in range(len(data)):
              if i % 2 == 0:
                     print(f"{i} is even")
              else:
                     pass

# Copy content from one file to another

with open("D:/Python Practice/Practice/HandleFile/Practice.txt","r") as f:
       with open("D:/Python Practice/Practice/HandleFile/copy.txt","w") as des:
              des.writelines(f.readlines())

# Append user input to a file

with open("D:/Python Practice/Practice/HandleFile/Practice.txt","a")as f:
       x = f.write("Elon Musk")
       print(x)

# Read a file, then go back to beginning and read again

with open("D:/Python Practice/Practice/HandleFile/Practice.txt","r")as f:
       print("\n1st read")
       data = f.read()
       print(data)
       
       f.seek(0)
       
       print("\n2nd read")
       data = f.read()
       print(data)

# Replace a word in a file

with open("D:/Python Practice/Practice/HandleFile/Practice.txt","r")as f:
        data = f.readlines()
with open("D:/Python Practice/Practice/HandleFile/Practice.txt","w")as wf:
       for dt in data:
           wf.write(dt.replace("Krushang","John"))

# Print pointer position

with open("D:/Python Practice/Practice/HandleFile/Practice.txt","r")as f:
    f.seek(10)
    x = f.read()
    print(x)

# Read last 10 characters of a file

with open("D:/Python Practice/Practice/HandleFile/Practice.txt", "r") as f:
    f.seek(0,2)
    size = f.tell()
    x = f.seek(size - 10)
    
    print(f.read())