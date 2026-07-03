import pandas as pd 

df1 = pd.DataFrame({"Name":['Rajat','Pal','Heera'],
                "toy":['car',None,'bike'],
                "buy":[None,None,'2026-03-26']
             })

print(df1.dropna(),'\n')
print(df1.fillna('-'))