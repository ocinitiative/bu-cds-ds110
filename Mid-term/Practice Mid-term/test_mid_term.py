# Use a while loop to print squares of integers, starting from 1, until the result is greater than 1234. (Don't print the square that is larger than 1234.


def some_squares_of_integers():
    i = 1
    while i ** 2 < 1234:
        print(i ** 2)
        i += 1

some_squares_of_integers()

# Write a function comma_sep_to_dict() that takes a string with comma-separated values as input, and stores the count of each comma-separated value in a dictionary, which is returned.  For example, "hello,hello,goodbye,goodbye" would result in a dictionary mapping "hello" to 2 and "goodbye" to 2.

def comma_sep_to_dict(s):
    d = {}
    for word in s.split(','):
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    return d

# In the Starbucks dataframe, print the Grande beverage with the most calories and the number of calories it has but not a function.

starbucks_df = pd.read_csv('starbucks_drinkMenu_expanded.csv')

starbucks_df[starbucks_df['Beverage_prep'] == 'Grande'].sort_values('Calories', ascending=False).head(1)


# Write a function all_have_digits() that takes a binary tree of the kind defined below and returns true if and only if every node in the tree has a string with a least one digit somewhere within the string.
# Should use python regular expressions to do this.
# Should use recursion to do this.

class BinaryTree:
  def __init__(self,left,right,s):
    self.left = left
    self.right = right
    self.s = s

# Test trees to help ... expect True for the first, False for the second
tree1 = BinaryTree(BinaryTree(None,None,"w3"),BinaryTree(None,None,"w2"),"w1")
tree2 = BinaryTree(tree1,BinaryTree(None,None,"w4"),"w")

import re

def all_have_digits(tree):
    if tree is None:
        return True
    elif re.search(r'\d', tree.s):
        return all_have_digits(tree.left) and all_have_digits(tree.right)
    else:
        return False














