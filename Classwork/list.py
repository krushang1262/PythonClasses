mylist = ["java","python","c++","ruby"]
print(mylist)

# allowed duplicate in list
mylist2 = ["Java","dotnet","Java","dotnet"]
print(mylist2)

language = ["Java","dotnet","Java","dotnet"]
print(len(language))
print(type(language))

#list constructor
myconst = list(("java","python","ruby","pearl"))
print(myconst)

#Access list
thislist = ["Java","Python","Mango","Banana","cherry","C#","php","bitcoin"]
print(thislist[1:4])
print(thislist[-1])
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])
if "Python" in thislist:
    print("yes")

# Change List and Add list Items

newList = ["Apple","Banana","Cherry","Mango","Graphes"]
newList2 = ["Rose","Sunflower","Mogra","Lilly"]
newList[2] = "Pineapple"
newList[2:4] = ["Orange","BlueBerry"]
newList[1:3] = ["Watermelon"]
newList.insert(1,"DragonFruit")
newList.append("Kiwi")
newList.extend(newList2)
print(newList)

# Remove List Items
remList = ["Mobile","Tablet","T.V","Games","Radio"]
remList.remove("T.V")
remList.pop(1)  # remove given index number value
remList.pop()   # remove last index nmber value
# del remList[1]
# del remList
remList.clear()
print(remList)

# Loop Lists
x = ["Samsung","Iphone","Vivo","Oppo","Realme"]
for i in x:
    print(i)

for i in range(len(x)):
    print(x[i])

i = 0
while i < len(x):
    print(x[i])
    i+=1

# List Comprehension

flower = ["rose","lilly","moghra","Sunflower","tulsi"]
newflower = []

for i in flower:
    if "r" in i:
        newflower.append(i)
    
print(newflower)

newflower = [x for x in flower if "a" in x]
print(newflower)

newflower = [x for x in flower if "rose" != x]
print(newflower)

n2 = ["a","b","c","d","e","f"]
s = []
s = [y for y in n2 if y not in "b"]
print(s)

n1 = [1,2,3,4,5,6]
value = []
value = [x for x in n1 if x >3 ]
print(value)

# Sort List Alphanumerically

lst = ["number","digit","string","char","float"]
lst.sort()
lst.sort(reverse=True)
print(lst)

lstnum = [5,6,4,7,3,9,1,2,20]
lstnum.sort()
print(lstnum)

lstnum.sort(reverse=True)
print(lstnum)

# Copy Lists

cpy = ["Film","Trailer","Teasor","Shooting","Editing"]
cpy2 = cpy.copy()
cpy1 = cpy[:]
print(cpy1, cpy2,end=" ")

# Join Lists

num = [1,2,3,4,5,6,7,8,9]
alpha = ["a","b","c","d","e","f","g","h","i"]

for i in alpha:
    num.append(i)
print(num)
    
for j in num:
    alpha.append(j)
print(alpha)

num.extend(alpha)
alpha.extend(num)
print(num)
print(alpha)

# list to tuple or tuple to list

tup = (1,2,3,4,5,6,7,8,9)
tup = list(tup)
tup.append(10)
tup = tuple(tup)
print("tup to list and list to tup",tup)