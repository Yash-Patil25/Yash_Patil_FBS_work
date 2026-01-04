#Create a class Shirt with members as sid,sname,type(formal etc), price and
#size(small,large etc) .Add following methods:
#g. Constructor (Support both parameterized and parameterless)
#h. Destructor
#i. ShowBook

class Shirt:
    def __init__(self,sid=0,sname="",stype="",price=0.0,size=""):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size
        print("Shirt Object created")

    def ShowBook(self):
        print("Shirt Id  :",self.sid)
        print("Shirt Name:",self.sname)
        print("Type      :",self.type)
        print("price     :",self.price)
        print("Size      :",self.size)

    def __del__(self):
        print("shirt Object Destroyed")

s1 = Shirt()
s1.ShowBook()

print()

s2 = Shirt(201,"Raymond","Formal",1999,"Large")
s2.ShowBook()