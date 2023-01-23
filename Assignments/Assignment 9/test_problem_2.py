# Advanced Pandas

import pandas as pd
import numpy as np

movies = pd.DataFrame({"Title": ["Perfect Blue",
                                 "Three Colours: Red",
                                 "Three Colours: Blue",
                                 "Three Colours: White",
                                 "Harold and Kumar Go to White Castle",
                                 "Men in Black",
                                 "Yellow Submarine"],
                       "Genre": ["Thriller","Drama","Drama","Drama","Comedy","Fantasy","Fantasy"],
                       "Year": [1997,1994,1994,1994,2004,1997,1968],
                       "Country": ["Japan","France","France","France","USA","USA","UK"],
                       "RTScore": [80, 100, 98, 87, 74, 92, 95]})

# Use pivot_table to create a table from the movies data where the rows are genres, the columns are countries, and the numerical values are average Rotten Tomatoes scores ("RTScore").







# Use groupby to find the mean score by genre.  Don't include averages of the year (use just the Genre and RTScore columns).
