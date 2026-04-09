import pandas as pd

df = pd.read_excel('~/Desktop/ClassExcelData/Main file.xlsx')

productTable = df[['Product','Category','Cost_per_box','PID']]
removeDup = productTable.drop_duplicates(subset=productTable)

locationTable = df[['Geo','Region','GID']]
removeDup1 = locationTable.drop_duplicates(subset=locationTable).sort_values(by='GID',ascending=True)

Sales_person_Table = df[['Sales_person','Team','Picture','SPID']]
removeDup2 = Sales_person_Table.drop_duplicates(subset=Sales_person_Table).sort_values(by='SPID',ascending=True)

Shipment_Table = df[['ShipmentID','SPID','PID','GID','Shipdate','Amount','Boxes','Order_Status']]
removeDup3 = Shipment_Table.drop_duplicates(subset=Shipment_Table).sort_values(by='ShipmentID', ascending=True)


loction_s = Shipment_Table.groupby('GID')['Amount'].sum().reset_index()
Report1 = pd.merge(removeDup1,loction_s,on="GID",how="inner")
Report1 = Report1[['Geo','Amount']]
# print(Report1)

sales = Shipment_Table.groupby('PID')['Boxes'].median().reset_index()
r1 = pd.merge(removeDup, sales, on='PID', how='inner')
r1['Sales & Costing'] = r1['Boxes'] * r1['Cost_per_box']
# print(r1,"\n")

topselling = removeDup.value_counts().head(5)
print(topselling,"\n")

Shipment_Table['Order_Status'] = Shipment_Table['Order_Status'].count()
countOrderStatus = Shipment_Table['Order_Status'].reset_index()
print(countOrderStatus)

