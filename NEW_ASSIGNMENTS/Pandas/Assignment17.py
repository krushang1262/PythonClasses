import pandas as pd 

# 17) Create a crosstab of the Make and Doors columns. 

data = {
    'Make': ['Toyota','Honda','Toyota','BMW','Honda','BMW','Toyota'],
    'Doors': [4,2,4,4,2,2,4]
}

dt = pd.DataFrame(data)

ct = pd.crosstab(dt['Make'], dt['Doors'])
print(ct)
