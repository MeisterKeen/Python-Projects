#
#   AUTHOR: Keen Little
#
#   DATE: 31 Marchh 2021
#
#   PURPOSE: Notes on object-oriented programming in Python
# 
# 
################################################################################


"""
Here is an example of creating a class with properties and methods:
"""

class User:
    # Define the attributes of the class
    name = "No Name Provided"
    email = ""
    password = "1234abcd"
    account = 0

    # Define the methods of the class:
    def login(self):
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email) == self.email and entry_password == self.password):
            print("Welcome back, {}".format(self.name))
        else:
            print("You are not authorized for this page.")

    # Here's a method to allow instantiating from this class:
    def __init__(self, name, email, password, account):
        self.name = name
        self.email = email
        self.password = password
        self.account = account

#Outside of the class you could create an instance of the User class
# new_user = User()
# Example:
New_user = User("John Doe", "jdoe@outlook.com", "p@ssw0rd", 1234)
# The dunder __init__() method above allows instantiating in one line:

#Call the login method using the new object
new.user.login()


"""
Example of creating a class with two child classes:
"""

class Vehicle:
    name = "None Entered"
    engine = ""
    manufacturer = "" # This could have dozens of properties

class Aircraft(Vehicle): # Note syntax, here >>> class Child(Parent):
    wingProfile = ""
    wingSpan = "" # These two properties add onto the three of the parent

class Boat(Vehicle):
    keelDepth = ""
    mastsNumber = ""


    
    
