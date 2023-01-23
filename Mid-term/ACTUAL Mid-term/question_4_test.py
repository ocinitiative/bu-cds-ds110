# Object

# Question 4

# Write a class Transaction that contains fields for a string name of the Transaction and a floating point amount of the Transaction.
# Also, write a constructor for this class that takes the name and amount as arguments and initializes the fields with those values.
# Write a method sum() that takes the present Transaction and another transaction (an argument) and returns the sum of their two values.  If the argument isn't a Transaction, throw a ValueError.
# Lastlt, write a function that isn't a method, sum_all(), that takes a list of Transactions as an argument, and returns their total sum. (You don't need to check the types of the items in the list.)

class Transaction:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
    def sum(self, other):
        if not isinstance(other, Transaction):
            raise ValueError
        return Transaction(self.name + ' + ' + other.name, self.amount + other.amount)

def sum_all(transactions):
    total = 0
    for t in transactions:
        total += t.amount
    return total
