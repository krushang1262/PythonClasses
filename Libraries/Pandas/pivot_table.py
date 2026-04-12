import pandas as pd 

df = pd.DataFrame({
    'Name': ['Amit', 'Amit', 'Raj', 'Raj'],
    'Month': ['Jan', 'Feb', 'Jan', 'Feb'],
    'Sales': [100, 150, 200, 250]
})

x = df.pivot_table(index='Name', columns='Month', values='Sales', aggfunc='mean')
print(x)