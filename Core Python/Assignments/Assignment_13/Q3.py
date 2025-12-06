#Python Program to Check if a Given Key Exists in a Dictionary or Not

my_dict = {'name': 'Yash', 'age': 21, 'course': 'python'}

key = input("Enter key to check:")

if key in my_dict:
    print("Key exists in the dictionary.")
else:
    print("key does NOT exists in the dictionary.")
