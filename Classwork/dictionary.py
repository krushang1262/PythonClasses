mydict = {
    "name":"Raj",
    "age":24,
    "email":"raj@gmail.com",
    "contact":8521479630,
    "age":35,
    "city":["london","japan","tokyo"]
}

print(mydict)
print(len(mydict))
print(type(mydict))

mydatadict = dict(name = "Krushang", age = 24, phone = 9874563210)
print(mydatadict)

# Access Dictionary Items

print(mydict["age"]) # if no key value is available give error
print(mydict.get("number")) # if no key is avilable give none 

x = mydict.keys()
y = mydict.values()
z = mydict.items()
print(x)
print(y)
print(z)

mydic = {
    "cast":"Open",
    "company":"XIT",
}

x = mydic.keys()
print(x)
mydic["phone"] = 88521479630
print(x)

y = mydic.values()
print(y)
mydic["city"] = "tokyo"
print(y)

z = mydic.items()
print(z)
mydic["Gender"] = "Male"
print(z)

if "company" in mydic:
    print(mydic["company"])
else:
    print("nope")

# Change and Add Dictionary Items

cd = {
    "brand":"BMW",
    "series":"x3",
    "color":"red"
}

cd["price"] = 120000000
print(cd)

cd.update({"brand":"G-wagon"})
print(cd)

# remove Dictionary Items

cd.pop("brand") # remove at the entered item
print(cd)

cd.popitem() # remove last item
print(cd)

del cd["color"]
print(cd)

cd.clear()
print(cd)

# Loop Dictionaries

for x in cd:
    print(x)

for y in cd:
    print(cd[y])

for a in cd.keys():
    print(a)
print('-------------------------------------------')

for b in cd.values():
    print(b)
print('-------------------------------------------')
for c in cd.items():
    print(c)

for d,e in cd.items():
    print(d,e)

# Copy Dictionaries

new = cd.copy()
print(new)

new1 = dict(cd)
print(new1)

# Nested Dictionaries

myfam = {
    "child1":{
        "name":"raja",
        "age":20
    },
    "child2":{
        "name":"khush",
        "age":21
    },
    "child3":{
        "name":"gita",
        "age":25
    },
    "child4":{
        "name":"om",
        "age":33
    }
}

print(myfam)
print(myfam["child2"])
print(myfam["child2"]["name"])

# Loop Nested Dictionaries

for x, obj in myfam.items():
    print('--------------------------')
    print(x)
    
    for y in obj:
        print(y + ':',obj[y])

mydata = {
    # "brand":"Honda",
    "model":"x-series"
}

mydata.setdefault("brand","Empty")
print(mydata)

x = mydata.setdefault("phone",9173789108)
print(x)