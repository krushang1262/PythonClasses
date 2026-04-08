import re

# requirement K,a,1_,@  .com   these are compulsory
email = input("Enter email to check: ")
pwdPattern = r"^[A-Za-z0-9_]+@[A-Za-z0-9]+\.(com)$"

if re.match(pwdPattern, email):
    print("valid")
else:
    print("not valid")