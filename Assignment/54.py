# 54) Write a Python program to check multiple keys exists in a dictionary 

dict = {"rose":1,"lilly":2, "moghra":3,"sunflower":4,"karen":5}

key_to_check = {"rose","lilly","galgoto","sunflower","karen"}

for key in key_to_check:
    if key in dict:
        print(f"{key} present in dictionary")
    else:
        print(f"{key} not present in dictionary")