class Calc:
    
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def __add__(self,other):
        return self.a + self.b + other.a + other.b
    
    def __mul__(self, other):
        return self.a * self.b * other.a * other.b

c = Calc(3,5)
x = Calc(4,6)
print(c+x)
print(c*x)