import numpy as np

a = np.array([
    [
        [1,2,3],
        [4,5,6]
    ],
    [
        [10,20,30],
        [40,50,60]
    ]
])


print(np.split(a,1, axis=0),"\n")
print(np.split(a,1, axis=1),"\n")
print(np.split(a,2, axis=0),"\n")
print(np.split(a,2, axis=1),"\n")

print("======array split============")
print(np.array_split(a,1, axis=0))
print(np.array_split(a,1, axis=1))
print(np.array_split(a,2, axis=0))
print(np.array_split(a,2, axis=1))
print(np.array_split(a,2, axis=2))