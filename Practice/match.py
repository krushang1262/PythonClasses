n1 = int(input("Enter number "))
mtch = input("Enter any operation ")
n2 = int(input("Enter number "))

match mtch:
    case "+":
        print(f"Addition is {n1+n2}")
    case "-":
        print(f"Subtraction is  {n1-n2}")
    case "*":
        print(f"Multiply is {n1*n2}")
    case "/":
        print(f"Divide is {n1/n2}")
    case _:
        print("invalid")    
    