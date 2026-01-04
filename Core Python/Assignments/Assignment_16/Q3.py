#Create a class Shirt with members as sid,sname,type(formal etc), price and size(small,large etc) .
# Add following methods: 
# j. Constructor (Support both parameterized and parameterless) 
# k. Destructor 
# l. ShowBook m. 
# For each size of shirt price should change by 10%. (eg. If 1000 is price then small price = 1000, medium = 1100,large=1200 and xlarge=1300) Use static concept.

class Shirt:
    
    size_price_factor = {
        "small": 0,
        "medium": 10,
        "large": 20,
        "xlarge": 30
    }

    def __init__(self, sid=0, sname="Not Assigned", stype="Casual",
                 price=0.0, size="small"):
        self.sid = sid
        self.sname = sname
        self.stype = stype
        self.price = price
        self.size = size.lower()
        self.apply_size_price()
        print("Constructor called")

    def apply_size_price(self):
        if self.size in Shirt.size_price_factor:
            increase = (self.price * Shirt.size_price_factor[self.size]) / 100
            self.price += increase

    def ShowBook(self):
        print("\nShirt ID:", self.sid)
        print("Shirt Name:", self.sname)
        print("Type:", self.stype)
        print("Size:", self.size)
        print("Price:", self.price)

    def __del__(self):
        print(f"Destructor called for Shirt ID: {self.sid}")

if __name__ == "__main__":
    s1 = Shirt()   
    s2 = Shirt(301, "Arrow", "Formal", 1000, "small")
    s3 = Shirt(302, "Peter England", "Formal", 1000, "medium")
    s4 = Shirt(303, "Louis Philippe", "Formal", 1000, "large")
    s5 = Shirt(304, "Raymond", "Formal", 1000, "xlarge")

    s1.ShowBook()
    s2.ShowBook()
    s3.ShowBook()
    s4.ShowBook()
    s5.ShowBook()
