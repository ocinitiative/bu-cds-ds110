# Write a function countdowns() that takes a list of integers as its sole argument.  The function should then print a "countdown" for each item in the list, starting from that number and ending in 0, with one number per line.

def countdowns(list):
    for i in list:
        for j in range(i, -1, -1):
            print(j)

# Write a function max_dict_merge() that takes two dictionaries as arguments and returns a third dictionary that is distinct from the other two (don't modify the input dictionaries).  If a key is in one of the dictionaries but not the other, that key should have the same value it had in its old dictionary in the new one.  But if the key was in both dictionaries, the new value in the new dictionary should be the max of the old values.

def max_dict_merge(dict1, dict2):
    dict3 = {}
    for key in dict1:
        if key in dict2:
            dict3[key] = max(dict1[key], dict2[key])
        else:
            dict3[key] = dict1[key]
    for key in dict2:
        if key not in dict3:
            dict3[key] = dict2[key]
    return dict3

# Using dataframe, a) Using the file genre_region_totals.csv, write code that prints the video game genre that sold the most worldwide.  (Note that "Worldwide" is a possible value for the region column.)

import pandas as pd

df = pd.read_csv('genre_region_totals.csv')

print(df[df['Region'] == 'Worldwide'].sort_values(by='Total', ascending=False).iloc[0]['Genre'])

# Now write code to print the "Puzzle" game sales in "North America".  (Hint: Your last step should be a call to loc[].)  The file has the sales records in millions, and you can keep them in that format.

print(df[(df['Genre'] == 'Puzzle') & (df['Region'] == 'North America')].iloc[0]['Total'])

