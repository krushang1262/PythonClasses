num = 121
temp = num
sum =0

while num !=0:
    rem = num%10
    sum = (sum*10)+rem
    num = num//10
    
if temp == sum:
    print("Armstrong")
else:
    print("Not Armstrong")
    
print("=====================Armstrong================================")

name = "loiol"

while name != '':
    rev = name[::-1]
    
    if rev == name:
        print("palindrome")
        break
    else:
        print("not palindrome")