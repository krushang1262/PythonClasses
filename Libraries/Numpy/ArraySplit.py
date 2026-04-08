import numpy as np

a = np.array([
    [
        [10,20,30],
        [50,60,70],
        [502,602,702],
    ],
    [
        [101,201,301],
        [501,601,701],
        [5011,6011,7011]
    ]
])

x = np.array_split(a,1, axis=2)
print("x array: \n\n",x)