n1 = int(input("Enter first number "))
n2 = int(input("Enter second number "))

# 2 Take a number from the user and print it.
print(f"number is {n1} and {n2}")

# 3 Take two numbers and print their sum.

print(f"sum of number is {n1+n2}")

#4 Take a number and check whether it is even or odd

if n1%2==0:
    print(f"{n1} Number is Even")
else:
    print(f"{n1} number is odd")
    
# 5 Take a number and check whether it is positive or negative.

if n1 > 0:
    print("Postive number")
else:
    print("Negative number")

# Loop Practice

#6 Print numbers from 1 to 10 using a loop.

for i in range(1,10):
    print(i)

#7 Print even numbers from 1 to 20.

for i in range(1,20):
    if i%2==0:
        print(f"{i} is Even")
    else:
        pass

#8 Print the table of a number entered by the user.

n1 = int(input("Enter number of table: "))
sum = 0
for i in range(1, 11):
    sum = n1*i
    print(sum)

#9 Find the sum of numbers from 1 to 100.

sum =0
for i in range(1,101):
    sum = i+sum
    print(sum)

#10 Print numbers from 10 to 1 (reverse order).

num = 10
while num !=0:
    print(num)
    num-=1

# Number Logic (Very Important)

# 11 Check whether a number is prime or not.

n1 = int(input("Enter a number to check it is prime or not "))
for i in range(2, n1):
    if n1 % i ==0:
        print(f"{n1} is prime")
        break
else:
    print(f"{n1} is not prime")

# 12 Find the factorial of a number

num = 7
sum = 1

while num !=0:
    sum = num * sum
    num-=1
print(sum)

# 13 Reverse a given number

num = 1,2,3,4,5,6
for i in num:
    print(num[::-i])
    break

# 14 Check whether a number is a palindrome

num = 121
temp = num
sum = 0

while num !=0:
    rem = num%10
    sum = (sum*10)+rem 
    num = num//10
    
if temp == sum:
    print("palindrome")
else:
    print("not palindrome")

# 15 Check whether a number is an Armstrong number

num = int(input("Enter the number: "))
dig = len(str(num))
temp = num
sum =0

while num !=0:
    rem = num%10
    sum = sum+(rem**dig)
    num//=10
    
if temp == sum:
    print("Armstrong")
else:
    print("not armstrong")

# List Logic

# 16 Create a list and print all elements

mylist = ["cat","bat","rat"]
print(mylist)

# 17 Find the largest number in a list.

mylen = [1,2,3,4,5,6,7,23,12]
print(max(mylen))

# 18 Find the smallest number in a list.

mysmllist = [12,5,4,3,6,7,9,8]
print(min(mysmllist))

# 19 Count how many even numbers are in a list.

myeven = [1,2,4,5,23,6,7,8,9,12,15,1,6,1,7,5]
sum = 0
for i in myeven:
    if i %2==0:
        sum +=1
print(f" total {sum} numbers are even in list")

# 20 Reverse a list without using reverse().

myrev = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
for r in myrev:
    print(myrev[::-r])
    break

# String Logic

# 21 Take a string and print each character

text = "Hello Bob what is update"

for t in text:
    print(t.strip())

# 22 Count vowels in a string.

text = str(input("Enter the character:").lower())
if text in ('a','e','i','o','u'):
    print("it is vowel")
else:
    print("not vowel")

# 23 Reverse a string python

st = "Python"
print(st[::-1])

# 24 Check whether a string is a palindrome

name = "RADAR"
text = name[::-1]

if name not in '':
    if name == text:
        print("Palindrome")
    else:
        print("not Palindrome")
    
# 25 Find the frequency of each character in a string

name = "raaaaaaadoo"
for i in name:
    print(f"{i} : {name.count(i)}")

# Logic Building (Beginner Friendly)

# star pattern

for i in range(1,5):
    print("*" * i)
    
for j in range(5,0,-1):
    print("*" * j)

# Print the number pattern

for i in range(1,5):
    for j in range(1, i+1):
        print(j)
    print()

# 28 Find the sum of digits of a number

num = 123456
sum =0

while num !=0:
    rem = num%10
    sum+=(rem)
    num//=10
print(sum)
    
# 29 Find the largest digit in a number

num = int(input("Enter the number here.. "))
largest = 0

while num !=0:
    digit = num %10
    if digit > largest:
        largest = digit
    num = num//10
print(largest)

# 30 Print Fibonacci series up to n terms.

n = int(input("Enter the numbers: "))

a=0
b=1
c=0
while c<=n:
    c=a+b
    a=b
    b=c
    print(c)