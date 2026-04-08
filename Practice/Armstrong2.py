num = int(input("Enter the number: "))
temp = num
dig = len(str(num))
sum = 0

while num != 0:
    rem = num%10
    sum+=(rem**dig)
    num = num//10
    
if temp == sum:
    print("Armstrong number")
else:
    print("Not armstrong")
    
print("===========================Armstrong 100 to 1000==========================================")    

for i in range(100,1000):
    num = i
    temp = num
    sum = 0
    
    while num !=0:
        rem = num%10
        sum +=(rem**3)
        num = num//10
    
    if temp == sum:
        print(f"{sum} Armstrong")
    else:
        pass