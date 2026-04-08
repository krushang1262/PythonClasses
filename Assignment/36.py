# 36) Write a Python function that takes a list and returns a new list with
# unique elements of the first list. 

def unique_element_list(ls):
    new_list=[]
    make_set = set(ls)
    new_list = list(make_set)
    return new_list

ls = ["Java","C#","Python","Ruby","C#","Python","Perl","Android","Python"]
uniqueElem =  unique_element_list(ls)
print(uniqueElem)