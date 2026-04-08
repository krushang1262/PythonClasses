for i in range(1,5):
    print("*" * i)
    
for i in range(5,0,-1):
    print("*" * i)

number = int(input("Enter the numbers: "))
for i in range(1, number +1):
    print(" " * (number - i) + "*" *(2*i-1))
