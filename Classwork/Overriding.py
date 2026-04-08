class Demo:
    
    def name(self):
        print("hello from demo class")
        
class sample(Demo):
    
    def name(self):
        print("hello from sample class")
        super().name()
        
s = sample()
s.name()