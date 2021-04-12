# ------- --------- --------- --------- --------- --------- --------- -------- 
# -------                       PYTHON NOTES                          --------
# -------            TECH ACADEMY SOFTWARE DEV BOOTCAMP               --------
# -------                       KEEN LITTLE                           --------
# ------- --------- --------- --------- --------- --------- --------- -------- 

# This document is a big disorganized mess -- some of it is just chunks of
# stuff from IDLE that I threw in because I wanted to be able to refer back
# to what I did. The rest is nicely commented but super basic.

# This big document helped me through my studies, so I'm sticking it in my
# GitHub as a way to remember my struggles.

# ------- --------- --------- --------- --------- --------- --------- -------- 
# -------                 BASIC NATIVE FUNCTIONS                      --------
# ------- --------- --------- --------- --------- --------- --------- -------- 



# print() -- prints a string, or a variable, or any data type
#
# type() -- will tell the type of data of a variable
#
# len() -- will tell the character length of a string
#
# NOTE: these functions are case-sensitive! Print() is not print()


# To create a variable:
variableName = "this is a string!"
otherVariable = 4
# No need to use a "var" or define the data type or length.

# examples:
myString = "hello world"
len(myString)
# This returns "11"

# Each character in a string is an element in a list!
# The list indexes from 0

# myString[0] would be "h"
# myString[4] would be "o"

# We can grab *negative* list items!
# myString[-1] grabs "d", the last list item
# myString[-3] grabs "r"
# So the last element in an array will be [-1] - nice shorthand, there.


# ------- --------- --------- --------- --------- --------- --------- -------- 
# -------              PRINT() TRICkS AND FORMATTING                  --------
# ------- --------- --------- --------- --------- --------- --------- -------- 

# We can concatenate strings:
fName = "Keen"
lName = "Little"

print(fName + lName)
# Result of that will be "KeenLittle"

# We can make it prettier:
print(fName + " " + lName)
# That gives us our space, "Keen Little"


# We can also format our print() command. Here's a trick:
print("Hello {} {}, welcome to Python!".format(fName, lName))
# This gives us a much nicer string:
# "Hello Keen Little, welcome to Python!"
 
# """Triple-quotes""" can be used to write a multi-line string

# \n is a newline character which affects how print() displays the line

# You can also create a long string using parens:
var3 = ("This string is too long to fit into one line of IDLE, "
"so I'll finish it on another line")


# ------- --------- --------- --------- --------- --------- --------- -------- 
# -------                      SLICING NOTATION                       --------
# ------- --------- --------- --------- --------- --------- --------- -------- 



var1 = "hello world"

var2 = var1[0:3]  # could also just say [:3] -- the zero is assumed
# var2 now contains "hel"

# I'll create an array:
numbers = [1 , 2, 3, 4, 5, 6, 7, 8]

# Now step through it with print() :
print(numbers[1:6:2])

# Returns 2, 4, 6
# We told py to "give me indexes one through six, incrementing by two"

# Try this:
print(numbers[1:6:3])
# Returns 3, 5


# ------- --------- --------- --------- --------- --------- --------- -------- 
# -------             MORE BASIC FUNCTIONS AND SYNTAX                 --------
# ------- --------- --------- --------- --------- --------- --------- -------- 



var5 = "hello"
print (var5.upper())
# Returns "HELLO"


# Keyword "in" can check if a substring is in a string:
var6 = "Have a free beer!"
print ("free" in var6)
# Returns "true"


# Using an "if" statement:
if "free" in var6: 
    print ("Yes, 'free' is present.")

if "blarg" not in var6:
    print ("blarg is not here")


# Looping through a string:
for x in "banana":
    print(x)

# Result:

# b
# a
# n
# a
# n
# a

# Where is the sentry, start, change and end in this "for" loop?
# Sentry is variable x
# Start is implied to be index [0]?
# End condition is length of the string -- because "in"?
# Incrementing the Sentry is implied?

# Escape character is backslash \
print("They call me \"Keen\" because that's my name")

# Dealing with data types:

num1 = "1" # this is a string
num2 = 2.1 # this is a float

print(num1 + num2) # throws an error, whoops

print(int(num1) + num2) # now we flip the "1" string to an int and it works




# ------- --------- --------- --------- --------- --------- --------- -------- 
# -------                        OPERATORS                            --------
# ------- --------- --------- --------- --------- --------- --------- -------- 

# ------- ARITHMETIC OPERATORS do basic arithmetic
# + , - , * , /    <--- obvious
# 
# %    <-- modulus. Divides and returns remainder. 
# **   <-- exponent. 10 ** 2 is ten SQUARED, result 100
# //   <-- floor division. Rounds result down to nearest integer.
#               ( / will return a float: 15 / 2 = 7.5 )

# ------- EXAMPLES:

num1 = 2
num2 = 2.1
print(num1 ** num2)

# Result 4.2870938501451725


# ------- ASSIGNMENT OPERATORS assign values to variables
# =     <--- equals
# +=    <--- add to! (x += 3) is same as (x = x+3) -- good for concatenation
# Each arithmetic operator can be done this way. Like **= or //=
# I don't understand these yet: &= , |= , ^= , >>= , <<=




# ------- BITWISE OPERATORS
# Holy shit
# &   <--- AND
# |   <--- OR
# ^   <--- XOR
# ~   <--- NOT
# <<  <--- Zero fill left shift
# >>  <--- Signed right shift

# I don't know how to use these???

# There are so many operators and I know how to use maybe 80% of them --
#   revisit this and fill out these notes later



# ------- --------- --------- --------- --------- --------- --------- -------- 
# -------        TUPLES, LISTS, SETS AND STRINGS, OH MY!              --------
# ------- --------- --------- --------- --------- --------- --------- -------- 

# ------- TUPLES:

# A tuple is a sequence of immutable objects (can't be changed).
# Lists can be changed, tuples can't.

# This is a tuple:
animal = ( 'zebra', 'alligator', 'giraffe', 'goat', 'ox')
# We aren't allowed to update or append to this.

# So let's make it a list:
listofAnimals = list(animal)
# Now we've spawned a list from the tuple!

print(listofAnimals)
['zebra', 'alligator', 'giraffe', 'goat', 'ox']
# The square brackets are a clue, here

# Now we can alter it:
listofAnimals.append ("honey badger")
print(listofAnimals)
['zebra', 'alligator', 'giraffe', 'goat', 'ox', 'honey badger']
# Try that with the animal tuple and it'll throw an error

# Here we can turn a string into a list:
myString = "Hello! I am pleased to meet you"
newString = list(myString)
print(newString)
['H', 'e', 'l', 'l', 'o', '!', ' ', 'I', ' ', 'a', 'm', ' ', 
'p', 'l', 'e', 'a', 's', 'e', 'd', ' ', 't', 'o', ' ', 'm', 'e', 'e', 't', 
' ', 'y', 'o', 'u']
# What a mess!

# Let's use the split() function to clean this up:
newString = myString.split(" ")
print(newString)
['Hello!', 'I', 'am', 'pleased', 'to', 'meet', 'you']
# Much better


# More play with lists:
myList = [2,3,4]
myList.append(5)
print(myList)
[2, 3, 4, 5]
# Simple enough, you can manipulate lists all sorts of ways.

# Traversing a list with a for loop:
myList.append(5)
for i in myList:
	print(i)
	
2
3
4
5

# Reverse the contents of a list:
myList.reverse()
print(myList)
[5, 4, 3, 2]

newString.reverse()
print(newString)
['you', 'meet', 'to', 'pleased', 'am', 'I', 'Hello!']

# make a copy of a list:
copyList = myList.copy()
print(copyList)
[5, 4, 3, 2]

# Two more useful methods for lists and tuples:
myList.count(2) # how many 2's appear in myList? result: 1
mylist.index(2) # where in myList does 2 appear?


# ------- SETS

mySet = {'baseball', 'basketball', 'football', 'hockey'}
len(mySet)
4
>>> mySet[0]
Traceback (most recent call last):
  File "<pyshell#178>", line 1, in <module>
    mySet[0]
TypeError: 'set' object is not subscriptable
>>> mySet.append("soccer")
Traceback (most recent call last):
  File "<pyshell#179>", line 1, in <module>
    mySet.append("soccer")
AttributeError: 'set' object has no attribute 'append'
>>> mySet.update("soccer")
>>> mySet
{'s', 'c', 'baseball', 'hockey', 'e', 'r', 'football', 'o', 'basketball'}
>>> mySet = {'baseball', 'basketball', 'football', 'hockey'}
>>> mySet.remove("baseball")
>>> mySet
{'hockey', 'basketball', 'football'}
>>> mySet.add("soccer")
>>> mySet
{'hockey', 'soccer', 'football', 'basketball'}
>>> mySet.difference(mySet)
set()
>>> otherSet = ('baseball')
>>> mySet.difference(otherSet)
{'hockey', 'soccer', 'football', 'basketball'}
>>> myDictionary = {'index1' : 1, 'index2' : 2, 'index3' : 3}
>>> print(myDictionary)
{'index1': 1, 'index2': 2, 'index3': 3}
>>> myDictionary['index2']
2
>>> dic_users = {'em_1234' : {'fname' : 'Bob', 'lname' : 'Smith', 'phone' : '123-456-7890'}, 'em_1235' : {'fname' : 'Mary', 'lname' : 'Jones', 'phone' : '123-456-7890'}}
>>> print(dic_users['em_1235'])
{'fname': 'Mary', 'lname': 'Jones', 'phone': '123-456-7890'}

print('User: {} {}\nPhone: {}'.format(dic_users['em_1235']['fname'],dic_users['em_1235']['lname'],dic_users['em_1235']['phone']))
User: Mary Jones
Phone: 123-456-7890

# I didn't quite understand how fromkeys() worked:
x = ('fname', 'lname')
y = ('Mary', 'Watson')
MaryWatson = dict.fromkeys(x, y)
print(MaryWatson)
"""{'fname': ('Mary', 'Watson'), 'lname': ('Mary', 'Watson')}"""

# So dict.fromkeys() is a little more literal than I thought it was.


# The most common data types in Python are:

# String: Str - A sequence of characters surrounded by quotation marks.
# Float: A number with a decimal point.
# Boolean: Bool - A value that can be either True or False.
# Integer: Int – a whole number.
# List[]: A series of items.
# Tuple(): Lists that are immutable (can’t be altered).
# Dictionary{}: A special list where the first item is the key (a unique identifier for some item of data), and the second item is the value (the data that is identified by the key).


# A for loop:
i = 0
for i in range(10):
	print("{} iteration through the loop.".format(i))
	i += 1

"""
0 iteration through the loop.
1 iteration through the loop.
2 iteration through the loop.
3 iteration through the loop.
4 iteration through the loop.
5 iteration through the loop.
6 iteration through the loop.
7 iteration through the loop.
8 iteration through the loop.
9 iteration through the loop.
"""

# A while loop:
i = 0
while i < 10:
	print("{} iteration through the loop.".format(i))
	i += 1

"""
0 iteration through the loop.
1 iteration through the loop.
2 iteration through the loop.
3 iteration through the loop.
4 iteration through the loop.
5 iteration through the loop.
6 iteration through the loop.
7 iteration through the loop.
8 iteration through the loop.
9 iteration through the loop.
"""


"""
<> - angles
() - parens
[] - brackets
{} - curlies
"""


# infinite While loop:
go = True 
while go: # meaning: while go is True
    print('Hello!')
# This will produce infinite Hello!'s




# So let's use loops and if/else together:

mySentence = 'loves the color'
color_list = ['red', 'blue', 'green', 'pink', 'teal', 'black',]

def color_function(name):
    lst = []
    for i in color_list:
        msg = "{0} {1} {2}".format(name,mySentence,i)
        lst.append(msg)
    return lst

def get_name():
    go = True
    while go: # We're using this while loop to wait for input:
        name = input('What is your name? ')
        if name == '': # If name is empty:
            print("You need to provide your name!") 
        elif name == 'Sally': # We made an elif to catch a specific name 'Sally'
            print('Sally, you shall not pass!') # If 'Sally', then we're still waiting for acceptable input
        else: # Once the input is put in, we shut off 'go'
            go = False
    lst = color_function(name) #we pass the name into the color function and run it
    for i in lst: # color function returns to lst, so now we print it with a for loop:
        print(i)

get_name()




# lambda function: define a function in one line:
thingy = lambda x: print(x)
thingy("hello")
hello



loc1="Portland"
loc2="San Francisco"
loc3="Seattle"
print("I flew from {0} to {1} to {2}".format(loc1,loc2,loc3))


# Using format() to change the formatting of the number 4:
print("binary: {0:b}, hexadecimal: {0:x}, percentage: {0:%}".format(4))
"""binary: 100, hexadecimal: 4, percentage: 400.000000%"""
# Super interesting, I can use this to deliver a hex value where it's needed, or a binary

# More uses of format():
def getSum(num1,num2):
	answer = num1 + num2
	print("The answer is {}.".format(answer))
	
getSum(1,2)
"""The answer is 3."""

getSum(5,67)
"""The answer is 72."""


# Escape sequences:

# \t to create a tab
# \n to start a string on a new line
# \r for a carriage return

myString = ("This is my string. \n This is my string on a new line.\
    \n \t This is my string on a new lin and using a tab.")

print(myString)
#This is My String
#This is my string on a new line.
#    This is my string on a new line and using a tab.



# Opening and reading a file in the os:
import os

with open("test.txt", "r") as f:  # "with" is sorta like "while" -- another kind of loop
    data = f.read() # we read what is now in f, and put it into the variable "data"
    print(data) # now we get a readout of what was in test.txt
    f.close() # close it out to end the loop!




# SQL queries in Python!
import sqlite3

conn = sqlite3.connect('test.db')
with conn: # open the token or session of test.db
    cur = conn.cursor() # our "cursor" is now on our test.db, we can write SQL code:
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_persons( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT, \
        col_lname TEXT, \
        col_email TEXT \
        )")
    conn.commit()
conn.close()


conn = sqlite3.connect('test.db')
with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES (?, ?, ?)", \
                ('Sarah', 'Jones', 'sjones@gmail.com') )
    cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES (?, ?, ?)", \
                ('Sally', 'May', 'sallymay@gmail.com') )
    cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES (?, ?, ?)", \
                ('Kevin', 'Bacon', 'kbacon@rocketmail.com') )
    conn.commit()
conn.close()















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
        if (entry_email) == self.email and entry_password == self.password:
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


class Doggo:
    name = "Dog Name"
    goodBoy = True
    owner = "Owner Name"
    breed = ""

    def __init__(self, name, owner, breed):
        self.name = name
        self.owner = owner
        self.breed = breed

    def whozagooboy(self):
        print("You're a good doggie!")

Bruno = Doggo("Bruno", "Jane Smith", "Labradoodle")


class Toy(Doggo):
    smallDog = True

Lily = Toy("Lily", "Joe Lane", "Teacup Poodle")

"""
IMPORTANT NOTE:
If you want to call >>> whozagooboy()   you must call the name
of the OBJECT that was instantiated from the CLASS!
"""
Bruno.whozagooboy()








"""
Another example of using Python and Sqlite:
"""

import sqlite3
with sqlite3.connect('test_database.db') as connection:
	c = connection.cursor()
	c.executescript("""DROP TABLE IF EXISTS People;
CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT);
INSERT INTO People VALUES('Ron', 'Obvious', 42);
""")
#sqlite3.Cursor object at 0x0000016D1C522570
peopleValues = (('Luigi', 'Vercotti', 43), ('Arthur', 'Belling', 28)) # a tuple of tuples!
c.executemany("INSERT INTO People VALUES(?, ?, ?)", peopleValues)
#sqlite3.Cursor object at 0x0000016D1C522570


#Useful bit:

c.execute("SELECT FirstName, LastName FROM People WHERE Age > 30")
while True:
    row = c.fetchone()
    if row is None:
        break
    print(row)



# Building basic windows in tkinter using commands line by line in the shell!
# Holy shit, these things can be painted into an OS window item by item IN REAL TIME!

>>> from tkinter import *
>>> win = Tk()
>>> win=Tk()
>>> b1 = Button(win, text="One")
>>> win=Tk()
>>> b1 = Button(win, text="One")
>>> b2 = Button(win, text = "Two")



>>> from tkinter import *
>>> win = Tk()
>>> win=Tk()
>>> b1 = Button(win, text="One")
>>> win=Tk()
>>> b1 = Button(win, text="One")
>>> b2 = Button(win, text = "Two")
>>> b1.pack()
>>> b2.pack()
>>> b1.pack(side=LEFT)
>>> b2.pack(side=RIGHT)
>>> b2.pack(side=LEFT)
>>> b2.pack(side=LEFT, padx = 10)
>>> b1.pack(side=LEFT, padx = 10)
>>> win = Tk()
>>> b1 = Button(win, text="One")
>>> b2 = Button(win, text="One")
>>> b1.grid(row=1, column = 0)
>>> b2.grid(row=1, column = 0)
>>> b2.grid(row=1, column = 1)
>>> b2 = Button(win, text="Two")
>>> b2.grid(row=1, column = 1)
>>> b1.grid(row=0, column = 0)
>>> 1 = Label(win, text = "This is a label" )
SyntaxError: cannot assign to literal
>>> l = Label(win, text = "This is a label")
>>> l.grid(row=1, column=0)






# Tricks in using pack() painting:
# (execute line by line in IDLE)
win = Tk()
f = Frame(win)
b1 = Button(f, text="One")
b2 = Button(f, text="Two")
b3 = Button(f, text="Three")
b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack(side=LEFT)
l = Label(win, text = "This label is over all buttons")
l.pack()
f.pack()


b1.configure(text="Uno") # configure() will change the window properties in real time!

b1.configure(text="Uno") # So we can define a function for the button
def but1():
	print("Button one was pushed")

	
b1.configure(command=but1) # And assign that function as a command using configure()


# Now let's get user input

win = Tk() # fire up a window
v = StringVar() # initialize a variable
e = Entry(win, textvariable = v) # create the entry widget
e.pack() # paint the widget to the window

# Type something into the entry field, and then:
v.get()
# booyah. We could do var1 = v.get() and store the text entry in a variable!

v.set("This is set by the program") # will put text in the entry box



# Let's create a window with a listbox:

lb = Listbox(win, height=3) # make a list box -- a box that holds lists of strings!
lb.pack() # paint it to the window
lb.insert(END, "first entry") # add entries to the window!
lb.insert(END, "second entry")
lb.insert(END, "third entry")
lb.insert(END, "fourth entry") # Whoops, this fourth one falls off because it's only 3 lines high!
sb = Scrollbar(win,orient=VERTICAL) # So we make a scrollbar
sb.pack(side=LEFT, fill=Y) # paint the scrollbar in the window with vertical orientation
sb.configure(command=lb.yview) # set the scrollbar to the y-axis view of the listbox
lb.configure(yscrollcommand=sb.set) # set the listbox's y-scroll command to the scrollbar
# Working scrollbar!

# Now select an item in the list and type:
lb.curselection()
# It will create a tuple with the number of the item you selected, indexing from 0
# So if you selected the third item, you'll get >>> (2,)