class Calc:
    
    def __init__(self, x):
        self.x = x
        
    def __add__(self, other):
        return self.x + other.x
    
    def __mul__(self, other):
        return self.x * other.x
    
    def __div__(self, other):
        return self.x / other.x

c1 = Calc(5)
c2 = Calc(5)
print(c1.__add__(c2))
print(c1.__mul__(c2))
print(c1.__div__(c2))

class text:
    a = 10
    def __str__(self):
        return f"Hello World {self.a}"
    
t = text()
print(t)

class length:
    def __init__(self, a):
        self.a = a
        
    def __len__(self):
        return len(self.a)
    
l = length("Hello")
print(len(l))

class Equal:
    def __init__(self, a,b):
        self.a = a
        self.b = b
        
    def __eq__(self,other):
        return self.a == other.a and self.b == other.b
    
e = Equal(5,10)
e1 = Equal(5,10)
print(e == e1)

class sample:
    def __init__(self, a):
        self.a = a
        
    def __getitem__(self, index):
        return self.a[index]
    
    def __setitem__(self,a,b):
        self.a[a] = b
        
s = sample([1,2,3,4,5])
s[0] = 10
print(s[0])