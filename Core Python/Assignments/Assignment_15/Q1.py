#1. Create a class Book with members as bid,bname,price and author.Add following methods:
#a. Constructor (Support both parameterized and parameterless)
#b. Destructor
#c. ShowBook


class book:
    def __init__(self, bid=None, bname=None, price=None, author=None):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author

    def showBook(self):
        print("Book ID   :",self.bid)
        print("Book Name :",self.bname)
        print("Price     :",self.price)
        print("Author    :",self.author)

    def __del__(self):
        print("Book object destroyed")

print("Using Parameterized Constructor")
b1 = book(101, "Python Programming", 499, "Guido van Rossum")
b1.showBook()

print("\nUsing Parameterless Constructor")
b2 = book()
b2.bid = 102
b2.name = "Data Science"
b2.price = 599
b2.author = "James Smith"
b2.showBook()