st = "My name is Krushang Balajiwala from tops technology"

print(st.lower())
print(st.upper())
print(st.casefold())
print(st.capitalize())
print(st.title())
print(st.strip())
print(st.replace("a","A"))
print(st.find("Balajiwala"))
print(st.startswith("My"))
print(st.endswith("technology"))
print(st.split())
print(st.join("X C"))
print("abcdef".isalpha())
print("1234".isdigit())
print("123abc".isalnum())
print("abc".zfill(15))
print("xyz".center(19,"-"))

print("================================================================")

xyz = "hello iam good"
print(xyz[0:16].split())
print(xyz[5:10].split())
print(xyz[2:10:2].split())
print(xyz[2::].split())
print(xyz[::2].split())
print(xyz[::-1].split())
print(xyz[-1::].strip())

print("================================================================")

record = "Data Analysis from tops technology"
word = record.split()

for i in word:
    print(i[::-1], end=" ")