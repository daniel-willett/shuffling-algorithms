#!/usr/bin/python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import subprocess
import time

try:
    subprocess.run(["./generator"], check=True)
except:
    subprocess.run(["go build generator.go"], shell=True, check=True)
    time.sleep(5)
    subprocess.run(["./generator"], shell=True, check=True)


data = pd.read_csv("results.csv", header=None)

matrix = np.zeros((52,52))

for pos in range(52):
    count = data[pos].value_counts()
    
    for card, cardCount in count.items():
        matrix[pos, card-1] = cardCount

probabilityMatrix = matrix/len(data)

plt.figure(figsize=(20,20))

upperLimit = np.max(probabilityMatrix)
lowerLimit = np.min(probabilityMatrix)

sns.heatmap(
        probabilityMatrix,
        cmap="RdYlGn",
        center=1/52,
        vmin=lowerLimit,
        vmax=upperLimit,
        )

plt.title("Card Positional Probability After Shuffling")
plt.xlabel("Card Number")
plt.ylabel("Original Position")

plt.show()





