# num = int(input("Enter a new num "))
# temp = num
# dig = len(str(num))
# sum = 0

# while num !=0:
#     rem = num%10
#     sum += (rem**dig)
#     num = num//10
    
# if temp == sum:
#     print("Armstrong")
# else:
#     print("Not Armstrong")
    
print("===================================================")

for i in range(100,1000):
    num = i
    temp = num
    sum = 0
    
    while num !=0:
        rem = num %10
        sum+=(rem**3)
        num = num//10
    
    if temp == sum:
        print(f"{temp} Armstrong")
    else:
        pass
        # print(f"{temp} not Armstrong")
        