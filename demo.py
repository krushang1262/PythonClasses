import pandas as pd 
import matplotlib.pyplot as plt

screen_time = [28, 32, 35, 26, 30, 68, 31, 29]

plt.title("weekly screen time (in hours) past 8 weeks")
plt.ylabel("screen time (in hours)")
plt.boxplot(screen_time)
plt.xticks([1],['My Screen Time'])
plt.show()