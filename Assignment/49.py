# 49) Write a Python script to concatenate following dictionaries to create a new one. 

d1 = {"apple":1, "banana":2, "cherry":3, "Mango":4}
d2 = {"a":4,"b":3,"c":2,"d":1}
d3 = {"mobile":5, "tablet":4, "smartwatch":3,"laptop":2,"cpu":1}

new_dict = {}

new_dict.update(d1)
new_dict.update(d2)
new_dict.update(d3)

print(new_dict)