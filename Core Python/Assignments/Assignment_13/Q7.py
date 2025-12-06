#Python Program to Remove the Given Key from a Dictionary

my_dict = {'name': 'Yash', 'age': 21, 'course': 'python'}

key = input("Enter the key to remove:")

if key in my_dict:
    del my_dict[key]
    print("Updated Dictionary:",my_dict)
else:
    print("key not found!!!")