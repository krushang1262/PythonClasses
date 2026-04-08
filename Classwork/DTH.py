num = 1101010
sum = 0
m = 1

while num !=0:
    rem = num%16
    sum = (rem*m)+sum
    num//=16
    m*10
print(sum)