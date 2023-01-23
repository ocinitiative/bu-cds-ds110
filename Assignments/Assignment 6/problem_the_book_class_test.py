# Problem 1 A


# Create a Book class with the following methods:
# A constructor that takes the author (string), title (string), and a list of ratings (integers)
# A `__str__()` method that returns the string "[title] by [author]" when invoked
# An `average_rating()` method that takes no argument and returns the average of all the ratings in the list
# A `rate()` method that takes one integer argument and adds that integer to the end of the ratings, returning the new list of ratings


class Book:
    def __init__(self, author, title, ratings):
        self.author = author
        self.title = title
        self.ratings = ratings

    def __str__(self):
        return f"{self.title} by {self.author}"

    def average_rating(self):
        return sum(self.ratings) / len(self.ratings)

    def rate(self, rating):
        self.ratings.append(rating)
        return self.ratings


# Problem 1 B

# Sometimes data for an entity can be spread across multiple records in the dataset.  Code the function merge() which takes two Book objects as arguments, and returns a single Book record where the author and title match the first argument, and the ratings are a concatenation of the two ratings lists.

def merge(book1, book2):
    return Book(book1.author, book1.title, book1.ratings + book2.ratings)


# Problem 1 C
# Code a class that inherits from Book, Nonfiction.  Give it a constructor identical to Book's, except it has one additional argument:  the edition number (an int).  Then add to the Nonfiction class a method more_recent_than() which takes a Book as an argument and returns true if 1) the authors and titles match, *and* 2) the Book calling it has a higher edition number than the argument.

class Nonfiction(Book):
    def __init__(self, author, title, ratings, edition):
        super().__init__(author, title, ratings)
        self.edition = edition

    def more_recent_than(self, book):
        return self.author == book.author and self.title == book.title and self.edition > book.edition
    

# Problem 1 D

# Code a class Fiction that inherits from Book and has an extra attribute *sequel*, which should be a Fiction (or None if there is no sequel).  Accept an extra argument in the constructor to set this attribute.  Throw a ValueError if the sequel argument isn't a Fiction object or None.
# Then write a method rest_of_series() that returns a list of the remaining titles in the series (as strings).  For example, if the Book The Fellowship of the Ring had the sequel The Two Towers, and that had a sequel of The Return of the King, then calling this method of The Fellowship of the Ring would return the list of strings ['The Two Towers', 'The Return of the King'].  (Your method should work with arbitrarily long chains of sequels, not just trilogies.)

class Fiction(Book):
    def __init__(self, author, title, ratings, sequel):
        super().__init__(author, title, ratings)
        if sequel is not None and not isinstance(sequel, Fiction):
            raise ValueError("Sequel must be a Fiction object or None")
        self.sequel = sequel

    def rest_of_series(self):
        if self.sequel is None:
            return []
        else:
            return [self.sequel.title] + self.sequel.rest_of_series()

# Problem 1 E

# Create a new BookDict class.
# The argument for the constructor should be the string name of a csv file.
# The csv columns in order from left to right are title, author, and a comma-separated string of ratings.
# The constructor should create a dictionary from title (string) to the Book object with that title.
# Call that dictionary my_dict and make it a field (attribute) of the BookDict object.
# (You can assume titles are unique for this exercise.
# Note that you will need to use the function float() to convert string ratings to floating point numbers.)
# The one other method for the BookDict, lookup(), should take a title (string) as an argument, and print the information stored in the Book for that title.
# The printed information should follow the format '[title] by [author] (average_rating)' -- for example, 'Pride and Prejudice by Jane Austen (4.2)'.
# Print no more than two digits after the decimal place. lookup() should also return the Book, besides printing its information.
# If the title isn't in the dictionary, print 'Not Found' and return None.  Use methods you have already created when you can.
# You can again assume titles are unique.

class BookDict:
    def __init__(self, filename):
        self.my_dict = {}
        with open(filename, "r") as f:
            for line in f:
                title, author, ratings = line.strip().split(",")
                self.my_dict[title] = Book(author, title, [float(rating) for rating in ratings.split("|")])

    def lookup(self, title):
        if title in self.my_dict:
            book = self.my_dict[title]
            print(f"{book.title} by {book.author} ({book.average_rating():.2f})")
            return book
        else:
            print("Not Found")
            return None

    

