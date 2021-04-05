
import os
import tkinter as tk
from tkinter import *

# We are using Python to generate an .html document,
# and then write in a string which is a very basic website.

# The text of the file to be written:
bigString = """
<html>
    <body>
        <h1>
{}
        </h1>
    </body>
</html>
"""

# Now we're going to create a tkinter box that the user can enter text into!

# Something isn't working. I'm not able to tie the buttons to functions,
# it seems, unless I define the thing as a class and give the class
# methods it can draw from. So I'm going to emulate an earlier exercise
# and borrow from its code to create my GUI.

class GuiWindow(Frame):

    def __init__ (self, master):
        Frame.__init__ (self)
        # Lookit me, putting it all in a proper frame and stuff!

        self.master = master
        self.master.resizable(width = True, height = True)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Create Your Web Page!')
        self.master.config(bg = '#0a63c8')

        # These buttons and things aren't pretty yet, will pretty-fy later
        # for some reason I'm getting errors when I try to use padx() and pady()

        self.l1 = Label(self.master, text = "What text do you want in your web page?")
        self.l1.grid(row=0, column=0)

        self.e1 = Entry(self.master, text = "page text...")
        self.e1.grid(row=1, column=0)

        b1 = Button(self.master, text = "Cancel", command = self.cancel)
        b1.grid(row=2, column=0, )

        b2 = Button(self.master, text = "Submit", command = self.submit)
        b2.grid(row=2, column=1, sticky=E)


    def submit(self):
        self.userText = self.e1.get()
        print(self.userText)
        self.makeHTML()

    def cancel(self):
        self.master.destroy()


# The script should then OPEN the file,
# it will appear in a new tab in my browser.

# STEPS: 1) create .html doc, 2) append text, 3) open file

    def makeHTML(self):
        doc = open("new.html", "w") # note the "w" here means to (over)write the file
        doc.write(bigString.format(self.userText)) # we will use "a" instead if we wish to append.
        doc.close()
        os.startfile("new.html") # here's why we had to import os

    # Maybe I should move that initial bigString into the class and rename it?

if __name__ == "__main__":
    root = Tk()
    App = GuiWindow(root)
    root.mainloop()

