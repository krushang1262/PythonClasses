# n = input("enter character: ")
# rev = ''

# for ch in n:
#     rev = ch + rev
    
#     if n==rev:
#         print("palindrome")
#     else:
#         print("not palindrome")
        
print("==========================================")

# name = "RADAR"
# sum = 0

# while name !='':
#     rev=name[::-1]
    
#     if rev == name:
#         print("palindrome")
#         break
#     else:
#         print("not palindrome")
# print("==========================================")


num = 121
temp = num
rev =0

while num !=0:
    rem = num %10
    rev = (rev*10)+rem
    num = num//10
    
if temp == rev:
    print("palindrome")
else:
    print("not palindrome")