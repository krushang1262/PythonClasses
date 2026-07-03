import pandas as pd 

employees = pd.DataFrame({'EmpID':[1,2,3,4,5,6,7,8,9,10],
                          'Name':["Krushang","Raj","Jeet","Mahesh","Alex","Ankit","Jay","Prakash","Vinay","Vishal"],
                          'Salary':[100,200,300,400,500,600,700,800,900,1000],
                          'DeptID':[1,2,3,4,3,1,4,1,2,3]})

department = pd.DataFrame({'DeptID':[1,2,3],'DeptName':['Accounts','HR','Sales']})

res = pd.merge(employees,department, on='DeptID',how='inner')
r1  = res[['EmpID','Name','DeptName']]
print(r1)