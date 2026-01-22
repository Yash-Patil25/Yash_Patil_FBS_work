#TKinter
# Develop a simple login system with a username and password field. Implement user
# authentication, and show a success message if the login is successful, or an error
# message if the login fails.

USERNAME = "admin"
PASSWORD = "12345"

username = input("Enter username: ")
password = input("Enter password: ")

if username == USERNAME and password == PASSWORD:
    print("Login Successful! Welcome,", username)
else:
    print("Login Failed! Invalid username or password")
