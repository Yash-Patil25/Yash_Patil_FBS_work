#Create a class Product with members as pid,pname,price and quantity .Add
#following methods:
#d. Constructor (Support both parameterized and parameterless)
#e. Destructor
#f. ShowBook

class Product:
    def __init__(self, pid=0,pname="",price=0.0,quantity=0):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity
        print("Product object created")

    def ShowBook(self):
        print("Product ID      :",self.pid)
        print("Product Name    :",self.pname)
        print("Product Price   :",self.price)
        print("Product Qunatity:",self.quantity)

    def __del__(self):
        print("Product object destroyed")

p1 = Product()
p1.ShowBook()

print()

p2 = Product(101,"Laptop",55000,2)
p2.ShowBook()