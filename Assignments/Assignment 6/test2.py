# Create another method for the BookDict, lookup(). It should take a title (string) as an argument, and print the information stored in the Book for that title. The printed information should follow the format '[title] by [author] (average_rating)' -- for example, 'Pride and Prejudice by Jane Austen (4.2)'.  Print no more than two digits after the decimal place.  lookup() should also return the Book, besides printing its information.  If the title isn't in the dictionary, print 'Not Found' and return None.

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