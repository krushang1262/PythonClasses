import pandas as pd 
import numpy as np

amount  = [100, 120, 105, 110, 5000, 115, 108]
print("average upi transaction (in ₹): ", np.mean(amount))
print("median upi transaction (in ₹): ", np.median(amount))