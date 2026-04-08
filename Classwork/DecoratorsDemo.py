def before(funct):
    def execute():
        print("before test calling")
        funct()
    return execute

@before
def newTest():
    print("newTest Calling")
    
newTest()

def add(func):
    def execute(*k):
        print(f"addition of {k[0]} and {k[1]} is {k[0] + k[1]}")
        func(*k)
    return execute
    
def mult(func):
    def execute(*k):
        print(f"multiplication of {k[0]} and {k[1]} is {k[0] * k[1]}")
        func(*k)
    return execute

@add
@mult
def calc(a,b):
    pass

calc(10,20)

def changeInfunc(funct):
    def execute(x):
        if str(x).isdigit():
            print("Valid")
        else:
            print("Invalid")
        funct()
    return execute

def myDigitFunc(*a):
    pass

myDigitFunc(55)

def myChar(fun):
    def execute(*k):
        if str(*k).isalpha():
            print("valid")
        else:
            print("Invalid")
        fun(*k)
    return execute

@myChar
def check(*a):
    pass

check("kdkkd")