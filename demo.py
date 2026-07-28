import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np 

import matplotlib.pyplot as plt


data = np.random.normal(loc=500,scale=100,size=1000)
mean = np.mean(data)
stdDev = np.std(data)

print("mean: ",mean,'\n',"Standaed Deviations",stdDev)

plt.hist(x=data, bins=30)
plt.show()


