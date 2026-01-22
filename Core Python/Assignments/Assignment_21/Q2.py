#Create class television that has members to hold the model number ,screen size
# and price. Take a member function to take input from user, If more than 4 digits
# are entered for model number, if screen size is smaller than 12 inches or greater
# than 70 inches or if the price is negative or greater than 5000 Rs, then throw an
# exception.
# Write a main() that instantiates an object and allows the user to enter and display
# data. If exception is caught, replace all data member values with zero

class Television:
    def __init__(self):
        self.model_no = 0
        self.screen_size = 0
        self.price = 0

    def get_data(self):
        try:
            self.model_no = int(input("Enter model number:"))
            self.screen_size = int(input("Enter screen size (in inches):"))
            self.price = float(input("Enter price (Rs):"))

            if self.model_no > 9999:
                raise ValueError("Model number should not be more than 4 digits")
            
            if self.screen_size < 12 or self.screen_size > 70:
                raise ValueError("Screen size must be between 12 and 70 inches")
            
            if self.price < 0 or self.price > 5000:
                raise ValueError("Price must be between 0  and 5000 Rs")
            
        except ValueError as e:
            print("Exception occurred:", e)

            self.model_no = 0
            self.screen_size = 0
            self.price = 0

    def display_data(self):
        print("\nTelevision Details")
        print("Model Number:",self.model_no)
        print("Screen Size:",self.screen_size, "inches")
        print("Price: Rs",self.price)

tv = Television()
tv.get_data()
tv.display_data()