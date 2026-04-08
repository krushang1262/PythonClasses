class Sample:
    __a = 10
    
    def get(self):
        print(self.__a)
        
    def set(self,a):
        self.__a = a
        print(a)
        
    def __display(self):
        print("sample display",self.__a)
        
sam = Sample()
sam.get()
sam.set(5)
sam.get()
print(dir(sam))
sam._Sample__display()