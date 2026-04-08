from multipledispatch import dispatch

class Sample:
    
    @dispatch(int,int)
    def add(self,a,b):
        print("addition method:",a+b)
       
    @dispatch(int,int,int) 
    def add(self,a,b,c):
        print("add method:",a+b+c)
        
s = Sample()
s.add(10,20)
s.add(10,20,30)