def is_prime(n):
    if n %2 == 0:
        return True
    else:
        return False
print(is_prime(4))


def count_vowels(s):
    x  = lambda s: f"{s} is Vowels" if 'a' in s or  'e' in s or  'i' in s or  'o' in s or  'u' in s else "Not Vowels"
    return x(s)

t = count_vowels('e')
print(t)
       

def reverse_words(s):
    word = s.split()
    rev_val = word[::-1]
    return " ".join(rev_val)
print(reverse_words("i love python"))


def second_largest(lst):
    removeFirstMax = max(lst)
    lst.remove(removeFirstMax)

    takeSecondMax = max(lst)
    return takeSecondMax

storeSecondMaxValue = second_largest([23,45,67,89,21,43,65])
print(storeSecondMaxValue)


def sum_digits(n):
    sum = 0
    if n < 0:
        return "number is negative"
    else:
        while n !=0:
            sum += n%10
            n//=10
        return sum
print(sum_digits(1234))

def char_freq(s):
    
    for i in s:
        print(f"{i} : {s[i]}")

char_freq({"a":2,"b":1,"c":3,"d":4})

def unique_order(lst):
    x = set(lst)
    y = list(x)
    print(y)
unique_order([2,3,4,5,4,3,2,6,7,8,7,9])
