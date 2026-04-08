class Demo:
    
    def __init__(self, name, salary=None):
        self.name = name
        self.salary = salary
        
        if self.salary is None:
            self.salary = self.salary = 0
        else:
            self.salary = self.salary
            
    def display(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
            
d1 = Demo("Krushang")
d2 = Demo("Raj", 50000)
        
d1.display()
d2.display()