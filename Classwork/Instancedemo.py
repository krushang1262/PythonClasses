class User:
    
    clgName = "DRB College" 
    def __init__(self,name,email):
        self.name = name
        self.email = email
    
    def myName(self):
        print(self.name,self.email,self.clgName)

User.clgName = "Rngpit Bardoli"
us = User("Krushang","Krushang@gmail.com")
us.myName()

us = User("Balajiwala","Balajiwala@gmail.com")
us.myName()