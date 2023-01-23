
# Create a new BookDict class.
# The argument for the constructor should be the string name of a csv file.
# The csv columns in order from left to right are title, author, and a comma-separated string of ratings.
# The constructor should create a dictionary from title (string) to the Book object with that title.
# Call that dictionary my_dict and make it a field (attribute) of the BookDict object. (You can assume titles are unique for this exercise.
# Note that you will need to use the function float() to convert string ratings to floating point numbers.)
# The one other method for the BookDict, lookup(), should take a title (string) as an argument, and print the information stored in the Book for that title.
# The printed information should follow the format '[title] by [author] (average_rating)' -- for example, 'Pride and Prejudice by Jane Austen (4.2)'.
# Print no more than two digits after the decimal place.  lookup() should also return the Book, besides printing its information.  If the title isn't in the dictionary, print 'Not Found' and return None.
# Use methods you have already created when you can.
# You can again assume titles are unique.


class BookDict:
    def __init__(self, csv_file):
        self.my_dict = {}
        with open(csv_file, 'r') as f:
            for line in f:
                line = line.strip()
                title, author, ratings = line.split(',')
                ratings = ratings.split()
                ratings = [float(rating) for rating in ratings]
                self.my_dict[title] = Book(title, author, ratings)

    def lookup(self, title):
        if title in self.my_dict:
            print(self.my_dict[title])
            return self.my_dict[title]
        else:
            print('Not Found')
            return None