import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sbn


def pandasPlot(data):
    data.plot.line()
    plt.figure(figsize=(8, 8))
    plt.xlabel('years')
    plt.ylabel('Development/year')
    plt.title("Development of whole data", fontsize=14, color="purple")
    plt.show()


dataset = pd.read_csv("worldDvp.csv")
matadata = dataset.iloc[0:9, 1:11]

matadataValue = matadata.iloc[0:9,1:11]
matadataValue


matadataNumVal = matadataValue[0:4]
matadataNumPercent = matadataValue[5:9]

data2010v = matadataNumVal['2010']
data2011v = matadataNumVal['2011']
data2012v = matadataNumVal['2012']
data2013v = matadataNumVal['2013']
data2014v = matadataNumVal['2014']
data2015v = matadataNumVal['2015']
data2016v = matadataNumVal['2016']
data2017v = matadataNumVal['2017']
data2018v = matadataNumVal['2018']


# plt.plot(data2010v)
# plt.plot(data2011v)
# plt.plot(data2012v)
# plt.plot(data2013v)
# plt.plot(data2014v)
# plt.plot(data2015v)
# plt.plot(data2016v)
# plt.plot(data2017v)
# plt.plot(data2018v)
# plt.show()


# or you may just plot in single line.
pandasPlot(matadataNumVal)

