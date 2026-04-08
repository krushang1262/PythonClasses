sum =0
for i in range(2,101):
    for j in range(2,i):
        if i%j==0:
            sum+=i
            print(i,"is prime")
            break

    else:
        print(i,"is not prime")
    
print(f"total prime no. is {sum}")