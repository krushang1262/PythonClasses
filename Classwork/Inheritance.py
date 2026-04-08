class Animal:
    
    def __init__(self,name,type):
        self.name = name
        self.type = type
    
    def display(self):
        print(self.name, self.type)
        
class Lion(Animal):
    def __init__(self, name, type,height,weight):
        super().__init__(name, type)
        self.height = height
        self.weight = weight
        
    def display(self):
        print(self.name,self.type,self.height,self.weight)

class Cat(Animal):
    pass

a = Animal("lion","wild")
a.display()  

l = Lion("Wolf","wild",50, 350)
l.display()  

c = Cat("Meow","domestic")
c.display()