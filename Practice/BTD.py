num = 11011101
sum = 0
power = 0

while num !=0:
        rem = num%10
        sum = sum + rem *(2 ** power)
        num//=10
        power+=1
print(f"{sum}")