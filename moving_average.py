import numpy as np

import matplotlib.pylab as plt
import pandas as pd


df = pd.read_csv(r"C:\Users\Ehsan\Desktop\AI_project\moving_average\project_data (1).csv")

kernel_size = 10
df["Moving_Average"] = df["<CLOSE>"].rolling(window=kernel_size).mean()


plt.figure(figsize=(10,5))
plt.plot(df["<CLOSE>"] , label = "main price" , alpha = 0.5 , color = "r")
plt.plot(df["Moving_Average"] , label = f"moving average ({kernel_size})" , color = "g")
plt.legend()
plt.title("Moving Average")
plt.show()
