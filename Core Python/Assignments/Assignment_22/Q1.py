#Pickling and Unpickling.

#Create a class Emp (eid,ename,basic)

class Emp:
    def __init__(self, eid, ename, basic):
        self.eid = eid
        self.ename = ename
        self.basic = basic

    def display(self):
        print("Emp ID:",self.eid)
        print("Emp name:",self.ename)
        print("Basic salary:",self.basic)


e1 = Emp(101,"Yash",2500)
e1.display()