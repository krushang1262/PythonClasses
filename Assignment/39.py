# 39)Write a Python program to find the second smallest number in a list.

smlst = [4,5,6,73,2,8,9,43,6]

small_num = min(smlst)
rem_small_num = smlst.remove(small_num)

new_min_num = min(smlst)
print(new_min_num)