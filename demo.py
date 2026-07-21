import pandas as pd 
import numpy as np

order_amounts = [180, 250, 310, 150, 420, 2200, 290, 340, 190, 210, 450, 380, 5100, 280, 350]

def val_outliers(data):
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)

    IQR = q3-q1
    LB = q1 - (IQR * 1.5)
    UB = q3 + (IQR * 1.5)

    outlier = [x for x in data if x < LB or x > UB]
    print(outlier)
    return outlier

val_outliers(order_amounts)