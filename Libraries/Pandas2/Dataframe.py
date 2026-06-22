import pandas as pd

# show data in table format row and columns

df = pd.DataFrame(
                    {'Name':['Krushang','Raj','yogesh'],
                   'RollNo':[1,3,5],
                   'Marks':[23,56,89]}
                )
print(df)