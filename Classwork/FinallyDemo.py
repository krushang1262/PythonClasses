def test():
    try:
        a = int(input("Enter number: "))
        return a
    except Exception as e:
        return e
    finally:
        print("test function ended")

k = test()
print(k)