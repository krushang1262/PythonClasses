# 9) Write python program that swap two number with temp variable and without temp variable.

a = int(input("Enter number1:"))
b = int(input("Enter number2:"))

temp = a
a = b
b =temp

print("After SWapping with temp")
print(f"{a}, {b}")

print("============================================")

x = int(input("Enter number1:"))
y = int(input("Enter number2:"))

x,y = y,x

print("After SWapping without temp")
print(f"{x}, {y}")