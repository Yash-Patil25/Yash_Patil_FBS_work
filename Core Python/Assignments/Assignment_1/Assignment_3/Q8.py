# Write a program to prompt user to enter userid and password. After verifying
# userid and password display a 4 digit random number and ask user to enter the
# same. If user enters the same number then show him success message otherwise
# failed. (Something like captcha)
import random
correct_userid = "admin"
correct_password = "1234"

userid = input("Enter user id:")
password = input("Enter password:")

if userid == correct_userid and password == correct_password:
    print("Login Successful! Now verify the captcha.")

    captcha = random.randint(1000, 9999)
    print("Captcha:",captcha)

    entered_captcha = int(input("Enter the above captcha number:"))

    if entered_captcha == captcha:
        print("Access Granted!.✅")
    else:
        print("Captcha verification failed.❌")
else:
    print("Invalid UserId or Password.❌")