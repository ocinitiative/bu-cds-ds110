# Seaborn

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



# Use the following code to load the data:

wine = pd.read_csv("winequality-red.csv", sep=";")
wine.head()

# Draw a 4-dimensional scatterplot of the data using the following features
# Alcohol for the x-axis, quality for the y-axis, volatile acidity for the hue, and sulphates for the size. 
# Set the sizes parameter to (10,400) to make those more visible. 
# You don't need to change the colormap or other defaults not mentioned here.

sns.scatterplot(x="alcohol", y="quality", hue="volatile acidity", size="sulphates", sizes=(10,400), data=wine)




