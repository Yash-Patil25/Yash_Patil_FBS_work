#Create a class Product with members as pid,pname,price and quantity .Add
#following methods:
#e. Constructor (Support both parameterized and parameterless)
#f. Destructor
#g. ShowBook
#h. Add static member discount.
#i. Provide methods for applying discount on price of product.

class Product:
    discount = 10   

    def __init__(self, pid=0, pname="Not Assigned", price=0.0, quantity=0):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity
        print("Constructor called")

    def ShowBook(self):
        print("\nProduct ID:", self.pid)
        print("Product Name:", self.pname)
        print("Price:", self.price)
        print("Quantity:", self.quantity)

    def apply_discount(self):
        discount_amount = (self.price * Product.discount) / 100
        self.price -= discount_amount
        print(f"Discount of {Product.discount}% applied")

    def __del__(self):
        print(f"Destructor called for Product ID: {self.pid}")


if __name__ == "__main__":
    p1 = Product()   
    p2 = Product(201, "Laptop", 60000, 2)  

    p1.ShowBook()
    p2.ShowBook()

    p2.apply_discount()
    p2.ShowBook()
