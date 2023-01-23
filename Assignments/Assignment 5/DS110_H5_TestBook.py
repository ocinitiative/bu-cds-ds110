# Problem 1

# check_alpha_or_digit():  True if the string is composed only of lowercase or uppercase letters *or* if the string is composed entirely of numerical digits (a mix of the two returns False).

def check_alpha_or_digit(s):
    if s.isalpha():
        return True
    elif s.isdigit():
        return True
    else:
        return False

# Problem 2

# well_trimmed(): True if the string contains no whitespace of the kind that would be removed by strip().  False if it contains leading or trailing whitespace.

def well_trimmed(some_string):
    if some_string.strip() == some_string:
        return True
    else:
        return False

# Problem 3

# is_ok():  True if the string contains any number of 'o's (but at least one) followed by a 'k'.  Case shouldn't matter, nor should any leading or trailing characters.  (Hint: call lower() on the string to ignore case).

def is_ok(some_string):
    if some_string.lower().strip().count('o') >= 1 and some_string.lower().strip().endswith('k'):
        return True
    else:
        return False

# Problem 3 test cases

# C,8 points) is_oko: True if the string contains any number of 'o's (but at least one) followed by a "k.

def is_oko(some_string):
    if some_string.lower().strip().count('o') >= 1 and some_string.lower().strip().endswith('k'):
        return True
    else:
        return False



# Problem 4

# no_bad_words():  False if the string contains either of the words 'fudge' or 'shoot', where the u in fudge or o's in shoot could be repeated arbitrarily many times; True if neither questionable word is contained in the string.  Ignore case again, so capitalized or lowercase words are grounds for a False.

import re

def no_bad_words(some_string):
  
  pattern = '(fu+dge)|(shoo+t)'
  
  if re.search(pattern, some_string, re.IGNORECASE):
    return False
  else:
    return True


# Problem 5a

# A Write a function count_pokemans() that takes a comma-separated string of Pokémon names and returns the number of unique Pokémon mentioned.  (Not only could there be duplicates in the string, but there may be whitespace differences that shouldn't matter; be sure to use strip().)

def count_pokemans(some_string):
    return len(set(some_string.split(',')))

# Problem 5b

# Write a function pokemon_to_dict that takes as its only argument the name of a CSV file.  The CSV file has player names in its first column and comma-separated Pokemon lists as its second column.
# If the file isn't there, a FileNotFoundError should be handled by printing a message that states the particular filename in the argument wasn't found.
# A sample Pokémon CSV, pokemon.csv, has been provided for this part.

import csv

def pokemon_to_dict(filename):
    try:
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            pokemon_dict = {}
            for row in reader:
                pokemon_dict[row[0]] = row[1].split(',')
            return pokemon_dict
    except FileNotFoundError:
        print('File not found: {}'.format(filename))

    

# Problem 5c

# Write a function dict_to_json that takes a dictionary and a filename as an arguments a dictionary of the kind created in part (b) and an output filename; the function should write the JSON implied by the dictionary to the given filename.

import json

def dict_to_json(dictionary, filename):
    with open(filename, 'w') as f:
        json.dump(dictionary, f)


# Recitation 5

# Problem 1

# 1) Write a reqular expression that looks for the pattern "In a _____ in the ground" where the blank contains at least one "word"' character. (Note that the case must match.)

import re

# TODO

pattern = "In a     in the ground"
long_string = hobbit_beginning
result = re.search(long_string, pattern)
print(result.group())


# Try writing to file a JSON that uses the my_dict dictionary.

my_dict = {
    'colors': ['green, blue'],
    'descriptions': ['curly','clever']
}

with open('my_dict.json', 'w') as f:
    json.dump(my_dict, f)


# Read the json file back again and print the values associated with'colors'.

with open ('my_dict.json', 'r') as f:
    my_dict = json.load(f)
    print(my_dict['colors'])


