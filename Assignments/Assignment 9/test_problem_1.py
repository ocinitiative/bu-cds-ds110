# For each text description of a query, make the corresponding query in SQLite (in Python).  Be sure to upload the cities.db file first.  This file contains two tables, the cities table containing "name" (of city) and "population", and the "best_cities" table, containing "city" and "reason" (one reason it's a good city, according to the AFAR website).

import sqlite3
connection = sqlite3.connect('cities.db')

# Query: All the best cities where the reason is "Nightlife."

query = "SELECT city FROM best_cities WHERE reason = 'Nightlife';"

# Query: All the cities in the cities table that end in '-ton,' and their populations.

query = "SELECT name, population FROM cities WHERE name LIKE '%-ton';"

# Query:  city name, reason it's a good city, and population, from an inner join of the two tables.  (This should produce 5 American cities.)

query = "SELECT cities.name, best_cities.reason, cities.population FROM cities INNER JOIN best_cities ON cities.name = best_cities.city;"