# break continue pass

for i in range(10):
    if i ==5:
        break # condition match stop looping execution
    print(i)

    print("*************break*********************************************")

for i in range(11):
    if i == 6:
        continue
    print(i) # skip the particular execution
    print("*************continue*********************************************")

for i in range(12):
    if i ==8:
        pass
    print(i)