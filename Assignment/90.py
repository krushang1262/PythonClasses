# 90) Write python program that user to enter only odd numbers, else will raise an exception.

try:
    a = int(input("Enter only odd numbers: "))

    if a % 2 == 0:
        print("You entered an odd number:", a)
    else:
        raise Exception("Even number is not allowed")

except Exception as e:
    print(e)