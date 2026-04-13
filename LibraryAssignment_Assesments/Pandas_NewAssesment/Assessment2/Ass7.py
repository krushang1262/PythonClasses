import pandas as pd

# 7. Convert price columns to numeric (remove $ and commas).

df = pd.read_csv('~/Desktop/AssignmentData/Retail Data.csv')

nm = df[['Cost Price','Retail Price','Discount $', 'Order Total', 'Shipping Cost', 'Total']]
removespChar = str(nm).replace('$',' ').replace(',',' ')
print(removespChar)