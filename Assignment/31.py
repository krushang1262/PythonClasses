# 31 Write a Python program to count the number of strings where the string
# length is 2 or more and the first and last character are same from a given list
# of strings.

text = ["RadR","Krushang","tezt","HocH"]
for t in text:
    if len(t) == 2 or len(t) > 2:
        if t[:1] == t[-1:]:
            print(f"{t} : {t.count(t)}")
        else:
            print(f"1 st and last letter are not same in these string {t}")
    else:
        print("length of string is less than 2")