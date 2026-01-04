#Create a class Book with members as bid,bname,price and author.Add following methods:
#a. Constructor (Support both parameterized and parameterless)
#b. Destructor
#c. ShowBook
#d. Add static variable count and also maintain count of objects created.

class Book:
    count = 0
    def __init__(self, bid=0, bname="Not Assigned", price=0.0, author="Unknown"):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author
        Book.count += 1
        print("constructor called")

    def ShowBook(self):
        print("\nBook ID    :",self.bid)
        print("Book Name    :",self.bname)
        print("Book Price   :",self.price)
        print("Book Author  :",self.author)

    def __del__(self):
        print(f"Destructor called for Book ID: {self.bid}")

if __name__ == "__main__":
    b1 = Book()
    b2 = Book(101, "Python Programming", 550.75, "Guido van Rossum")

    b1.ShowBook()
    b2.ShowBook()

    print("\nTotal Book object created:",Book.count)