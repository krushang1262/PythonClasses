num = 89101112
decimal = 0
power = 0

while num !=0:
    rem = num%10
    decimal = decimal + rem *(8 ** power)
    num //=10
    power +=1
print(f"{decimal} octal to decimal conversion")
    