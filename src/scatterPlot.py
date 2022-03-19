import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sbn
from bokeh.palettes import magma


def scatter(x, y):
    colr = magma(36)
    plt.xlabel('years')
    plt.ylabel('developments')
    plt.title("Scattered data of dataset", fontsize=14, color="black")
    plt.scatter(matadataNumVal, matadataNumPercent, color=colr)
    plt.show()

################# main body ###############################

dataset = pd.read_csv("worldDvp.csv")
matadata = dataset.iloc[0:9, 1:11]

matadataValue = matadata.iloc[0:9,1:11]
matadataValue


matadataNumVal = matadataValue[0:4]
matadataNumPercent = matadataValue[5:9]

scatter(matadataNumVal, matadataNumPercent)














