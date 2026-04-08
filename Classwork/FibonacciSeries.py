n = int(input("Enter your number here: "))
x=0
y=1
z=0

while z<=n:
    print(z)
    x=y
    y=z
    z=x+y
    
print("=========================================") 
a=0
b=1
for i in range(100):
    c = a+b
    print(c)
    a=b
    b=c