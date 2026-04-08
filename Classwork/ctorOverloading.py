class ctorOverloading:
    
    def __init__(self, name, age=None):
        self.name = name
        self.age = age
        
    def show(self):
        print("Name:",self.name)
        print("Age:",self.age)
        
cc = ctorOverloading("Krushang")
cc1 = ctorOverloading("Raj", 25)
cc.show()
cc1.show()