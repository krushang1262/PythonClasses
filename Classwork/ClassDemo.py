class MyPen :
    
    company = "cello"
    price = 120
    color = "black"
    expDt = 0
    
    def writeText(self):
        print(f"company is {self.company}, color is {self.color}, price is {self.price},expire date is {self.expDt}")
    
p1 = MyPen()
p1.price = 50
p1.writeText()

p2 = MyPen()
p2.expDt = "12/6/2026"
p2.writeText()