# 55)Write a Python script to merge two Python dictionaries

student = {"name": "Krushang", "age": 23, "course": "D.A","Fees":85000}
duration = {1:2,3:4,5:6,7:8,9:10}

new_dict = {}

new_dict.update(student)
new_dict.update(duration)
print(new_dict)