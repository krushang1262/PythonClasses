import pandas as pd

index1 = [('America',2020), ('Japan',2021), ('India',2022), ('China',2023), ('Europe',2024), 
        ('America',2021), ('Japan',2022), ('India',2023), ('China',2024), ('Europe',2025)]

populations = [123456789, 789654123,258963147,4569871230,3214789650,128456789, 989654123,258966147,4569871220,32789650]

df = pd.Series(populations, index=index1)
print(df)

classes = [('A',1),('A',2),('A',3),('B',1),('B',2),('B',3)]
mks = [20,30,25,26,34,22]

x = pd.Series(mks, index=classes)
print(x)