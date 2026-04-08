class Car:
    
    def __init__(self,name,series,price):
        self.name = name
        self.series = series
        self.price = price
    
    def cardetails(self):
        print(self.name,self.series,self.price)
        
        
class cartype(Car):
    
    def __init__(self, name, series,price,carType,mileage,engineType):
        super().__init__(name, series,price)
        
        self.carType = carType
        self.mileage = mileage
        self.engineType = engineType
    
    def cardetails(self):
        print(self.name,self.series,self.price, self.carType,self.mileage,self.engineType, end=" ")

prc = cartype("BMw","x-series",4500000000,"Sport-car",349,'power Engine')
prc.cardetails()