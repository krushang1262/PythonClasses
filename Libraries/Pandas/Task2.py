import pandas as pd

df = pd.read_excel('~/Desktop/ClassExcelData/Main file.xlsx')

productTable = df[['Product','Category','Cost_per_box','PID']]
removeDup = productTable.drop_duplicates(subset=productTable)
print(removeDup,"\n")

locationTable = df[['Geo','Region','GID']]
removeDup1 = locationTable.drop_duplicates(subset=locationTable).sort_values(by='GID',ascending=True)
print(removeDup1,"\n")

Sales_person_Table = df[['Sales_person','Team','Picture','SPID']]
removeDup2 = Sales_person_Table.drop_duplicates(subset=Sales_person_Table).sort_values(by='SPID',ascending=True)
print(removeDup2,"\n")

Shipment_Table = df[['ShipmentID','SPID','PID','GID','Shipdate','Amount','Boxes','Order_Status']]
removeDup3 = Shipment_Table.drop_duplicates(subset=Shipment_Table).sort_values(by='ShipmentID', ascending=True)
print(removeDup3)


loction_s = Shipment_Table.groupby('GID')['Amount'].sum().reset_index()
Report1 = pd.merge(removeDup1,loction_s,on="GID",how="inner")
Report1 = Report1[['Geo','Amount']]
print(Report1)






