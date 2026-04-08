st = "Sun rises in the east and good morning"

print(st.lower())
print(st.upper())
print(st.casefold())
print(st.capitalize())
print(st.title())
print(st.strip())
print(st.replace('s','c'))
print(st.find("morning"))
print(st.startswith("Sun"))
print(st.endswith("morning"))

print(st.split(" "))
print(st.join("KC"))
print("abcde".isalpha())
print("12563".isdigit())
print("and12563".isalnum())
print("abc".zfill(15))
print("abc".center(15,"-"))

print("=======================================================")

k = "helloiamfromtopsinstitutebatchdataanalatics"
print(k[0:7])
print(k[1:5])
print(k[5:])
print(k[2:9:3])
print(k[-1])
print(k[::-1])

data = "Sun rises in east"
word = data.split(" ")
for i in word:
    print(i[::-1],end=" ")