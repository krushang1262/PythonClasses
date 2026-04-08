key = [2,3,4,5,6,7]
k = map(lambda a:a*a,key)
print(list(k))

subject = ["java","python","c#","Php","nodejs"]
s = map(lambda a:len(a), subject)
print(list(s))

a = [10,20,30,40,50]
b = [1,2,3,4,5]

k = map(lambda x,y:x*y,a,b)
print(list(k))