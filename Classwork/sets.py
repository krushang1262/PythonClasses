thisset = {"rose","lilly","mogra"}
print(thisset)

# duplicate not allowes

numset = {10,20,20,30,10}
print(numset)

# Note: The values True and 1 are considered the same value in sets, and are treated as duplicates

num1set = {"apple","mango",True,1,2}
print(num1set)

# Note: The values False and 0 are considered the same value in sets, and are treated as duplicates:

numfalse = {"apple","mango",0,True}
print(numfalse)

# length of sets

mylen = {"apple","banana","cherry"}
print(len(mylen))

# Data Types

s1 = {"cat","bat","rat"}
s2 = {1,2,3,4}
s3 = {True, False,False,True}
print(s1,s2,s3)

# type in set

set1 = {"abc",32, True,45,"male"}
print(type(set1))

# set Constructor

sc = set(("apple","mango","banana","cherry"))
print(sc)

# Access Items

sit = {"mango","apple","banana","cherry"}

for s in sit:
    print(s)
print("cherry" in sit)
print("grapes" not in sit)

# Add Items

myAdd = {"banana","cherry"}
myAdd.add("apple")
print(myAdd)

myupdateSet = {10,20,30,40,50}
mythisset = {40,60,70,80,100,90}

myupdateSet.update(mythisset)
print(myupdateSet)

# Add Any Iterable

myset = {"mexician","vadapav","dabeli"}
mylist = ["chinese","southindian"]

myset.update(mylist)
print(myset)

# Remove Set Items

remSet = {"banana","apple","cherry","mango","watermelon"}

remSet.remove("apple")
print(remSet)

remSet.discard("cherry")
print(remSet)

# pop

thispop = {"apple","mango","banana","cherry"}
x = thispop.pop()
print(x)
print(thispop)

# clear

myclr = {"srk","slmnkhn",'Imhsm','Ajdgn'}
myclr.clear()
print(myclr)

# del myclr
# print(myclr)

# Join Sets

num = {1,2,3,4,5}
alpha = {"a","b","c","d","e"}

print(num.union(alpha))
num.update(alpha)
print(num)

# tuple and set implementation

s1 = {1,2,3,4}
s2 = ("apple","banana","cherry")
print(s1.union(s2))

# Intersection

sint = {1,2,4,5,6}
uint = {2,7,8,9,1}
print(sint.intersection(uint))

# intersection_update

s = {'a','b','c','d'}
f = {'x','y','z','a'}

s.intersection_update(f)
print(s)

# difference
sdiff1 = {"apple","mango","banana", True}
sdiff2 = {"cherry","mango","pineapple"}

sdiff1.difference(sdiff2)
print(sdiff1)

# difference_update

sd = {"apple","mango","banana"}
sd2 = {"apple","lichi","kiwi"}

sd.difference_update(sd2)
print(sd)

# symmetric_difference()

st = {"apple","banana","cherry"}
st2 = {"pineapple","kiwi","apple"}

st3 = st.symmetric_difference(st2)
print(st3)

# symmetric_difference_update() remove the duplicate from the both sets

s1 = {"krushang","jayesh",",milen"}
s2 = {"krushang","hasan","keyu"}

s1.symmetric_difference_update(s2)
print(s1)

# frozenset

f = frozenset({"apple","cherry","mango"})
d = frozenset({"cherry","mango","leather"})
cp = f.copy()
print(type(f))
print(cp)
print(f.difference(d))

# intersection

n = frozenset({1,2,3,4,5})
n1 = frozenset({4,5,6,7,8})

print(n.intersection(n1))

# isdisjoint

print(n.isdisjoint(n1))
print(n1.isdisjoint(n))

# issubset

print(n.issubset(n1))
print(n1.issubset(n))

# issuperset
print(n.issuperset(n1))
print(n1.issuperset(n))

# symmetric_difference

print(n.symmetric_difference(n1))

# union
print(n.union(n1))
