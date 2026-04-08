for i in range(2,101):
    for j in range(2,i):
        if i%j==0:
            print(f"{i} is prime")
            break
        
    else:
        print(f"{i} is not prime")