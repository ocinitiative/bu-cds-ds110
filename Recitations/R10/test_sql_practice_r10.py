# SQL

# Using SQL to complete the following question

# Read the books.db file and create a database connection

import sqlite3
connection = sqlite3.connect('books.db')

import pandas as pd
pd.read_sql('SELECT * FROM titles', connection)

# Retrieve all title and edition info for books with strictly more than 3 editions.

pd.read_sql('SELECT * FROM titles WHERE editions > 3', connection)

# Retrieve the titles and copyrights of books that contain the word "Visual" and have a copyright year of 2015 or earlier.

pd.read_sql('SELECT title, copyright FROM titles WHERE title LIKE "%Visual%" AND copyright <= 2015', connection)

# Retrieve all titles that don't include the words "How to".

pd.read_sql('SELECT * FROM titles WHERE title NOT LIKE "%How to%"', connection)

# Retrieve the 3 titles and copyrights with the most recent copyright.

pd.read_sql('SELECT title, copyright FROM titles ORDER BY copyright DESC LIMIT 3', connection)