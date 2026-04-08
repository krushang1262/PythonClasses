# marks = int(input("Enter your Marks: "))

# if marks>=90 and marks <=100:
#     print("Grade A++")
# elif marks>=85 and marks <=89:
#     print("Grade A")
# elif marks>=75 and marks <=84:
#     print("Gade B+")
# elif marks >=69 and marks <=74:
#     print("Grade B")
# elif marks >=50 and marks <=59:
#     print("Grade C")
# elif marks >=40 and marks <=49:
#     print("Grade D")
# elif marks <40:
#     print("You are Failed!")

# print("********************match catch********************************")

# choice =  int(input("Enter your choice"))
# match choice:
#     case 1:
#         print("gujarati")
#     case 2:
#         print("hindi")
#     case 3:
#         print("english")
#     case 4:
#         print("marathi")
#     case _:
#         print("Invalid choice")

# print("********************match catch*****calc***************************")

num1 = int(input("Enter number 1: "))
operation = input("Added a Calculation method ")
num2 = int(input("Enter number 2: "))

match operation:
    case "+":
        print("Added value is",num1+num2)
    case "-":
        print("minus value is",num1-num2)
    case "*":
        print("multiply value is",num1*num2)
    case "/":
        print("division value is",num1/num2)
    case _:
        print("Invalid opeation your perform")