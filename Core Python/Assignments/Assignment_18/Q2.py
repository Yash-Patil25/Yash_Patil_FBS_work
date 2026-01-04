#Create a class Distance with data members as km,m and cm and add following
#methods :
#a. Constructor
#b. Destructor
#c. Overload +,- operator

class Distance:

    def __init__(self, km=0, m=0, cm=0):
        self.km = km
        self.m = m
        self.cm = cm
        self._normalize()

    def _normalize(self):
        self.m += self.cm // 100
        self.cm = self.cm % 100

        self.km += self.m // 1000
        self.m = self.m % 1000

    def __add__(self, other):
        result = Distance(
            self.km + other.km,
            self.m + other.m,
            self.cm + other.cm
        )
        return result

    def __sub__(self, other):
        total_cm1 = (self.km * 100000) + (self.m * 100) + self.cm
        total_cm2 = (other.km * 100000) + (other.m * 100) + other.cm

        diff_cm = abs(total_cm1 - total_cm2)

        km = diff_cm // 100000
        diff_cm %= 100000
        m = diff_cm // 100
        cm = diff_cm % 100

        return Distance(km, m, cm)

    def show(self):
        print(f"{self.km} km {self.m} m {self.cm} cm")

    def __del__(self):
        print("Distance object destroyed")

if __name__ == "__main__":
    d1 = Distance(2, 450, 80)
    d2 = Distance(1, 550, 40)

    print("Distance 1:")
    d1.show()

    print("Distance 2:")
    d2.show()

    print("Addition:")
    d3 = d1 + d2
    d3.show()

    print("Subtraction:")
    d4 = d1 - d2
    d4.show()
