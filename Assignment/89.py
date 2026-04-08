# 89) How Do You Handle Exceptions with Try/Except/Finally in Python? 
# Explain with coding snippets. 

try: 
    a = 10
    a/=2
    print(a)
except Exception as e:
    print(e)
finally:
    print("finally part is execute")