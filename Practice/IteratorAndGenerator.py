l = [1,2,3,4,5]
k = iter(l)

print(next(k))
print(next(k))
print(next(k))

# generator

def my_gen(s):
    for i in range(s):
        yield i+i
        
t = iter(my_gen(10))
print(next(t))
print(next(t))
print(next(t))
print(next(t))