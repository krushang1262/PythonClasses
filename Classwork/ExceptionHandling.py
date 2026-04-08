try:
    a=10
    a/=2
    print(a)
except Exception as e:
    print(e)
else:
    print("No exception are phase")
finally:
    print("program ended")

print("program ended")

try:
    a = 10
    # print(k)
    print(a)
    a = 21+"wsc"
except Exception as e:
    print(e)
except NameError as n:
    print(n)