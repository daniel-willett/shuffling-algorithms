#!/usr/bin/python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import subprocess
import time

"""
try:
    subprocess.run(["./generator"], check=True)
except:
    subprocess.run(["go build generator.go"], shell=True, check=True)
    time.sleep(5)
    subprocess.run(["./generator"], shell=True, check=True)
"""


data = pd.read_csv("results.csv", header=None)

matrix = np.zeros((52,52))

for pos in range(52):
    count = data[pos].value_counts()
    
    for card, cardCount in count.items():
        matrix[pos, card-1] = cardCount

probabilityMatrix = matrix/len(data)

plt.figure(figsize=(16,12))
sns.heatmap(
        probabilityMatrix,
        cmap="RdYlGn",
        center=1/52,
        vmin=0.015,
        vmax=0.024,
        )

plt.title("Card Positional Probability After Shuffling")
plt.xlabel("Card Number")
plt.ylabel("Original Position")

plt.show()





