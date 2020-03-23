#plotting the graphs using matplotlib

import matplotlib.pyplot as plt
import pandas as ps
import numpy as ny

#create a simple bar and scatter plot

x = ny.arange(5)
y = (20,35,30,35,27)
plt.bar(x,y)
print(plt.bar(x,y))
