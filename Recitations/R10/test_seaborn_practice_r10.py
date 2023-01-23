# Seaborn Practice from Recitation 10

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Something to know about the data:
# The Titanic dataset contains information about the passengers who were on board the Titanic when it sank.  We'll be using it as a dataset to practice using Seaborn.  Some columns of interest are:

# survived:  0 if the passenger didn't survive, 1 if they did.
# sex:  male or female.
# age:  In years.
# class:  First, Second, or Third - First Class was the fanciest.

# Read the data from the file
titanic_df = sns.load_dataset("titanic")

titanic_df.head() # What is this doing? 
# It's showing the first 5 rows of the dataframe

titanic_df.dtypes # What is this doing?
# It's showing the data types of each column

# Create a bar plot to bar plot using seaborn to illustrate the effect of class on the survival rate.
# There should be three bars, one for First, Second, and Third Class, and their heights should be the average survival rates.

sns.barplot(x="class", y="survived", data=titanic_df)

# Create a faceted diagram (displot) where the two rows correspond to male and female
# The three columns are First, Second, and Third Class, and the plots are bar graphs showing age.



# Create a second faceted diagram in which the row is still sex, the column indicates whether the person survived, and the plotted value is the age.
# Do the smoothed kernel density estimation (kind="kde") to plot smoothed curves.
# Write some code here















