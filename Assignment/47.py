# 47)How will you create a dictionary using tuples in python?

x = [("a",1),("b",2),("c",3),("d",4),("e",5)]
y = dict(x)
print(y)

new = {k:v for k,v in x}
print(new)