import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sbn


def HistOfWorldDevp(data):
    sbn.histplot(data, kde=True, bins=11, alpha=1)
    plt.xlabel('years')
    plt.ylabel('developments')
    plt.title("World Development", fontsize=18, color="red")
    plt.show()


dataset = pd.read_csv("worldDvp.csv")
matadata = dataset.iloc[0:9, 1:11]

matadataValue = matadata.iloc[0:9,1:11]
matadataNumVal = matadataValue[0:4]

HistOfWorldDevp(matadataNumVal)