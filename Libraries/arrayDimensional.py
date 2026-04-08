import numpy as np

a = np.array([1,2,3,4])
print(a)
print(a.ndim)
print(a.shape)
print(a.size)

b = np.array([
        [1,2,3],
        [4,5,6]
])
print(b.ndim)
print(b.size)
print(b.shape)

c = np.array([
    [
        [1,2,3],
        [4,5,6]
    ]
])

print(c.ndim)
print(c.size)
print(c.shape)

d = np.array([
    [
        [
            [1,2,3,4],
            [5,6,7,8]
        ],
        [
            [11,12,13,14],
            [15,16,17,18]
        ]
    ]
])
print(d.ndim)
print(d.size)
print(d.shape)