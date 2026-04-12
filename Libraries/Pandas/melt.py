import pandas as pd 

df = pd.DataFrame({
    'Name': ['Amit', 'Amit', 'Raj', 'Raj'],
    'Month': ['Jan', 'Feb', 'Jan', 'Feb'],
    'Sales': [100, 150, 200, 250]
})

x = pd.melt(df, id_vars='Name', var_name='Month')
print(x)