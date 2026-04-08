from functools import reduce

# 1 Lambda से किसी number का cube निकालिए

def my_lam(a):
    res = lambda a:a**3
    return res(a)

print(my_lam(24))

# 2 Lambda से check करें number positive है या negative

def my_num(x):
    res = lambda x: "Negative number" if x <0 else "Positive number"
    return res(x)

print(my_num(2))
print(my_num(-12))

# 3 Lambda से दो strings में से बड़ी length वाली string return करें

def lambi_str(a,b):
    res = lambda x,y: x if len(a) > len(b) else y
    return res(a,b)

print(lambi_str("Krushang","bala"))

# 4 Lambda से check करें string palindrome है या नहीं

def my_pal(a):
    data = lambda a: "Palindrome" if a == a[::-1] else "Not Palindrome"
    return data(a)
print(my_pal("radar"))

# 5 Lambda से check करें number divisible by 3 और 5 दोनों से है या नहीं

def my_num5or3(a):
    res = lambda a: f"{a}" if a%3==0 and a%5==0 else "not divisible"
    return res(a)

print(my_num5or3(15))
print(my_num5or3(10))
    
# Lambda + map()

# 6 List के हर number का square निकालिए

l = [2,4,6,8,12,16,20]
res = map(lambda x:x*x,l)
print(list(res))

# 7 List के हर element में 5 add कीजिए

l = [2,4,6,8,12,16,20]
res = map(lambda a:a+5,l)
print(list(res))

# 8 Strings की list को uppercase में बदलिए

lst = ["Hello","Python","Java","Nodejs","Ruby","Perl"]
res = map(lambda a:a.upper(),lst)
print(list(res))

# 9 Numbers की list को absolute values में बदलिए

nums = [2, -4, 5, -7, -10]
res = map(lambda a:abs(a),nums)
print(list(res))

# Lambda + filter()
# 10 List में से सिर्फ even numbers निकालिए

ls = [2,23,4,5,6,7,8,98,12,32,43]
res = filter(lambda a:a%2==0,ls)
print(list(res))

# 11 List में से सिर्फ positive numbers निकालिए

ls = [12,34,56,-1,-34,-56,41,-90-78]
res = filter(lambda a:a > 0,ls)
print(list(res))

# 12 Strings की list में से सिर्फ length > 4 वाली strings निकालिए

ls = ["Hello","java","Python","Ruby","Node","Flutter"]
res = filter(lambda a:len(a) > 4, ls)
print(list(res))

# 13 List में से सिर्फ prime numbers filter कीजिए


# Lambda + reduce()
# 14 List के सभी numbers का sum निकालिए

ls = [5,6,7,5,4,3,8,9]
key = reduce(lambda a,b: a+b,ls)
print(key)

# 15 List के सभी numbers का product निकालिए

ls = [3,4,5,6,7]
k = reduce(lambda a,b: a*b,ls)
print(k)

# List में से maximum number निकालिए (without max())

ls = [2,4,1,5,22,3,1,3]
key = reduce(lambda a,b: a if a > b else b ,ls)
print(key)

# Mixed Logic (Medium)
# 17 List of tuples को second element के आधार पर sort कीजिए

tup_list = [(1, 5), (3, 2), (4, 9), (2, 1)]
srt = sorted(tup_list, key=lambda x:x[1])
print(srt)

# 18 List of strings में से longest string निकालिए

lonstr = ["Hello","Python","Java","Android","Ios"]
for u in lonstr:
    k = reduce(lambda a,b: a if len(a) > len(b) else b, lonstr)
print(k)

# 1️9️ List के numbers को odd और even में अलग कीजिए

oelst = [1,2,3,4,5,6,7,8,9,10]
k = map(lambda a: f"{a} is even" if a%2==0 else f"{a} is odd",oelst)
print(list(k),end=" ")

# 2️0️ List में से duplicate values हटाइए (lambda allowed)

lst = [2,3,4,5,6,7,8,4,5,6,2]
print(list(set(lst)))