# 57) Write a Python program to find the highest 3 values in a dictionary
dic = {"apple":10, "mango":20, "cherry":30, "watermelon":40}

all_dict_values = list(dic.values())

first_max_value = max(all_dict_values)
remove_first_max_value = all_dict_values.remove(first_max_value)

second_max_value = max(all_dict_values)
remove_second_max_value = all_dict_values.remove(second_max_value)

third_max_value = max(all_dict_values)
print(f"3 Higest value: {third_max_value}")