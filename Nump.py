from numpy import random
import matplotlib.pyplot as plt
import seaborn as sea


data={
    "narmal":random.normal(loc=50, scale=5, size=1000),
    "binormial":random.binomial(n=100, p=0.5, size=1000)
}


sea.displot(data, kind="kde")
plt.show()