def my_func():
    print("Hello World!")
my_func()

# with parameter

def my_num_param(n1,n2):
    print(f"sum of num is {n1+n2}")
my_num_param(10,20)

# return type

def my_return(a,b,c):
    return a+b+c
    
r = my_return(2,2,2)
print(r)

def my_square(x,y):
    sq = x*y/x+y
    return sq
sq = my_square(45,36)
print(sq)

def my_total(a,b,c):
    return a+b+c

def my_percentage(a):
    return ((a*100)/150)

t = my_total(23,65,78)
p = my_percentage(t)
print(p)

# default function 

def my_def_fun(name,email="testing",phone=0):
    print(name,email,phone)
    
my_def_fun("Krushang","Balaji@gmail.com")
my_def_fun("Krushang")
my_def_fun("Krushang",phone="4563217896")

# # tuple as param

def my_tup(*a):
    sum = 0
    for i in a:
        sum +=i
    print(sum)
my_tup(22,3,4,4,5,5,5,3333,3,32)

# # dict as param

def my_dict(**c):
    print(c)
    
my_dict(name="Krushang",email="k@gmail.com",phone=7412589630,address="Katargam surat")

# # local and global

a= 100
def my_loc_glob():
    global a
    a = 500
    print(f"inside func {a}")
    
my_loc_glob()
print(a)

# # lambda

def my_lam(a):
    return a*a

my_lam = lambda a:a*a
print(my_lam(25))

# calc program

def my_calculator():
    n1 = int(input("Enter first number: "))
    opt = input("Added a Calculation method: ")
    n2 = int(input("Enter second number: "))
    
    match opt:
        case "+":
            print(f"Addition of two num is {n1+n2}")
        case "*":
             print(f"Multiply of two num is {n1*n2}")
        case "-":
             print(f"Subtraction of two num is {n1-n2}")
        case "//":
             print(f"Division of two num is {n1//n2}")
        case _:
            print("Invalid operation u perform")
    return opt
    
my_calculator()

# recursion
# 
def my_recursion(num):
    print(num * num)
    num+=1
    
    if num <=10:
        my_recursion(num)
    
my_recursion(10)