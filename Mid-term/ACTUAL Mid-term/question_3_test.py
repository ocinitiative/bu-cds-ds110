# Using the file genre_region_totals.csv, write code that prints the video game genre that sold the most worldwide.  (Note that "Worldwide" is a possible value for the region column.)
# Pandas is required for this question.
# The columns of the CSV file are: genre, region, sales

import pandas as pd

df = pd.read_csv('genre_region_totals.csv')
df = df[df['region'] == 'Worldwide']
print(df[df['sales'] == df['sales'].max()]['genre'].values[0])

# Write code to print the number of sale of "Puzzle" game in "North America".
# Should use the call loc[]
# Using the file genre_region_totals.csv, write code that print the "Puzzle" (this is a genre) game sales in "North America" (this is a region).
# Pandas is required for this question.

import pandas as pd

df = pd.read_csv('genre_region_totals.csv')
print(df.loc[(df['genre'] == 'Puzzle') & (df['region'] == 'North America'), 'sales'].values[0])