num = 128
temp = num
sum =0

while num !=0:
    rem = num%10
    sum = (sum*10)+rem
    num = num//10
    
if temp == sum:
    print(f"{temp} is palindrome")
else:
    print(f"{temp} not palindrome")
    
print("==================================================")

num = "radar"
rev = ''

while num != '':
    rev= num[::-1]

    if rev == num:
        print(f"{rev} palindrome")
        break
    else:
        print(f"{rev} not palindrome")