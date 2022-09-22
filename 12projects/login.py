import time

username = "Hunaid"
password = "Password"

username_input = input('Username: ')
password_input = input('Password: ')

if username_input == username and password_input == password:
    print("Access Granted")
    print("please wait")
    time.sleep(5)
    print("Loading......")
    time.sleep(3)
    print("You are successfully logged in")

elif username_input == username and password_input != password:
    print("Password is incorrect")

elif username_input != username and password_input == password:
    print("Username is incorrect")

else:
    print("Please check both the fields")



