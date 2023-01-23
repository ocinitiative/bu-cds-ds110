# You work for the creators of Pokemon GO, a game where players try to collect odd-looking monsters called Pokemon by venturing to real-ife locations.
# You got a CSV file with each player's name followed by a list of Pokemon they' ve captured, but the list could contain duplicates. The goal is to create a JSoN file that maps each player to the number of unique Pokemon theyve captured.


# a)(10 points) Write a function count_pokemansO that takes a comma-separated string of Pokemon names and returns the number of unique Pokemon mentioned. (Not only could there be duplicates in the string, but there may be whitespace differences that shouldn't matter; be sure to use strip0.)

def count_pokemans(some_string):
    return len(set(some_string.split(',')))



# b) (14 points) Write a function pokemon_to_dict that takes as its only argument the name of a CSV file. The CSV file has player names in its first column and comma-separated Pokemon lists as its second column (see part a). (You can assume there is no header line that is different from all the others - all the lines contain data in the format described.) The function should return a dictionary where the keys are player names, and the values are the number of unique Pokemon associated with their player (see part a).
# If the file isn't there, a File NotFoundError should be handled by printing a message that states the particular filename in the argument wasn't found.
# A sample Pokemon CSV, pokemon. csv, has been provided for this part.

import csv

def pokemon_to_dict(filename):
    try:
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            pokemon_dict = {}
            for row in reader:
                pokemon_dict[row[0]] = count_pokemans(row[1])
            return pokemon_dict
    except FileNotFoundError:
        print('File not found: {}'.format(filename))






# c) (6 points) Write a function dict_to_ison that takes a dictionary and a filename as an arguments a dictionary of the kind created in part
# (b) and an output filename; the function should write the JSON implied by the dictionary to the given filename.

import json

def dict_to_json(dictionary, filename):
    with open(filename, 'w') as f:
        json.dump(dictionary, f)

        


# mydict = pokemon_to_dict('Pokemon.csv')
# dict_to_json(mydict, 'poke.json')
# !ls
# !cat poke.json   # Should be Alice: 7, Bob: 3, Carol: 3, Eileen: 3, Fatima: 5











# Use the following code box to upload the sample Pokemon.csv file, and include your final code for parts (a)-(c) in the code box after that.