# l = [1,2,3,4,5,6,7,8,9] # use all list, tuple, set, dict in iter
# k = iter(l)

# print(next(k))
# print(next(k))
# print(next(k))
# print(next(k))

#generator

def square(s):
    for i in range(s):
        yield i*i

t = iter(square(12))
print(next(t))
print(next(t))
print(next(t))
print(next(t))