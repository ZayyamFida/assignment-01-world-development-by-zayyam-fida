import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sbn



def pieChart2018(data, lbl):
    plt.title("Pie Chart of Word Development 2018", fontsize=14, color="green")
    plt.pie(data, labels=label, colors=colors, autopct='%.0f%%')
    plt.show()



dataset = pd.read_csv("worldDvp.csv")
matadata = dataset.iloc[0:9, 1:11]

matadataValue = matadata.iloc[0:9,1:11]
matadataValue


md_indic = matadata['Indicator Name']
label = md_indic[5:9]

matadataNumVal = matadataValue[0:4]
matadataNumPercent = matadataValue[5:9]
colors = sbn.color_palette('pastel')[0:5]

data = matadataNumPercent['2018']
pieChart2018(data, label)



