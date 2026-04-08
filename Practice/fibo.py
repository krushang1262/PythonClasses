n = int(input("Enter the number of fibo sequence: "))
a= 0
b= 1
c= 0

while a<=n:
    c=a+b
    print(c)
    a=b
    b=c

print("==================================================================")

x=0
y=1

for i in range(100):
    z=x+y
    print(z)
    x=y
    y=z