#Operator overloading.
#1. Create a class Complex Number with data members as real and imag and add
#following methods :
#a. Constructor
#b. Destructor
#c. Overload +,- operator

class ComplexNumber:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real,
                             self.imag + other.imag)
    
    def __sub__(self, other):
        return ComplexNumber(self.real - other.real,
                             self.imag - other.imag)
    
    def show(self):
        sign = '+' if self.imag >= 0 else '-'
        print(f"{self.real} {sign} {abs(self.imag)}i")

    def __del__(self):
        print("ComplexNumber object destroyed")

if __name__ == "__main__":
    c1 = ComplexNumber(4,5)
    c2 = ComplexNumber(2,3)

    print("First Complex NUmber:")
    c1.show()

    print("second complex number:")
    c2.show()

    print("Addition")
    c3 = c1 + c2
    c3.show()

    print("Subtraction")
    c4 = c1 - c2
    c4.show()