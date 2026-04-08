# 58)Write a Python program to combine values in python list of dictionaries.

sample_data = [{'item': 'item1', 'amount': 400},
               {'item': 'item2', 'amount': 300},
               {'item': 'item1', 'amount': 750}]
result = {}

for k in sample_data:
    x = k['item']
    y = k['amount']
    
    if x in result:
        result[x] += y
    else:
        result[x] = y

print(result)