
txt = 'w3resource'
result = {}

for ch in txt:
    if ch not in result:
        result[ch] = 1
    else:
        result[ch] +=1
print(result)