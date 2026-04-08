def count_val_num(n):
    if n <=0:
        print("negative val")
    else:
        print(n)
        count_val_num(n-1)

count_val_num(10)

def back_num_print(s):    
    if len(s) == 0:
        return 
    else:
        print(s[-1])
        back_num_print(s[:-1])
back_num_print("Krushang")


def num_sub(x):
    if x < 0:
        print("num is less than zero")
    else:
        if x > 10000:
            return x
        print(x)
        num_sub(x*10)
num_sub(10)

def min_num(n):
    if n == 0:
        return
    print(n)
    min_num(n-1)

print(min_num(10))

def tbl_func(n):
    if n == 0:
        return 1
    return n * tbl_func(n-1)

print(tbl_func(5))