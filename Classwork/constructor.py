class newClass:
    
    def __init__(self,name,email):
        self.name = name
        self.email = email
    
    def myFunc(self):
        # print("my function")
        print(self.name, self.email)
        
# n = newClass()
# n.myFunc()

nm = newClass("balu","balu@gmail.com")
nm.myFunc()