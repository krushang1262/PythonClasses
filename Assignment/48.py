# 48) Write a Python script to sort (ascending and descending) a dictionary by value. 

weeks_dic = {"Tuesday": 3, "Monday": 2,  "Thursday": 5,  "Wednesday": 4, "Sunday": 1,  "Saturday": 7,"Friday": 6}

asc = sorted(weeks_dic.items(), key=lambda i:i[1])
print(asc)

desc = sorted(weeks_dic.items(), key=lambda x:x[1], reverse=True)
print(desc)