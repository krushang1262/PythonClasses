num = 1569
temp = num
digit = len(str(num))
rev = 0

while num !=0:
    rem = num%10
    rev+=(rem**digit)
    num = num//10
    
if temp == rev:
    print("armstrong")
else:
    print("not armstrong")
    