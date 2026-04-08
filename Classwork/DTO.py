num = 1011101
sum = 0
m = 1

while num !=0:
    rem = num%8
    sum = (rem*m)+sum
    num//=8
    m*=10
print(sum)