import pandas as pd 

df = pd.read_csv('~/Desktop/DataSheet/diamonds.csv')

caratColor = df[(df['carat']>0.5) & (df['color']=='D') | (df['color']=='E') | (df['color']=='F')]
caratCutWise = caratColor.groupby(['color','cut'])['price'].sum()
resetIndex = caratCutWise.reset_index()
sort = resetIndex.sort_values(by=['color','price'], ascending=[True,False])
changeColmn = sort.rename(columns={'color':'COLOR','cut':'CUT','price':'Total Price'})
print(changeColmn)