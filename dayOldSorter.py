import os, time, shutil
import tkinter as ik
from tkinter import *
from tkinter import filedialog

sourcePath = ""
destPath = ""

def browseSource():
    global sourcePath
    sourcePath = filedialog.askdirectory(initialdir = "C:/Users/",
                                         title = "Select a Directory")
    browse1.configure(text = sourcePath)

def browseDest():
    global destPath
    destPath = filedialog.askdirectory(initialdir = "C:/Users/",
                                         title = "Select a Directory")
    browse2.configure(text = destPath)

def fileMover():
    files = os.listdir(sourcePath)
    for file in files:
        filePath = sourcePath + "/" + file
        timeNow = time.time()
        fileTime = os.stat(filePath).st_mtime
        timeFloat = timeNow - fileTime
        timeHours = timeFloat // 3600
        if timeHours > 24:
            shutil.move(filePath, destPath)
    

# Just laying out my GUI here:
window = Tk()
window.title('layout, woo')
window.geometry("500x300")
window.config(background = "lightgray")


# First label, which should display the selected path
select1 = Label(window,
                text = "Select Directory to Move Day-Old Files From:",
                width = 70, height = 2,
                fg = "blue",
                bg = "lightgray")
select1.grid(column = 0,
             row = 0)


# Here's our BROWSE button, we'll attach the file-browser function here:
browse1 = Button(window,
                 text = "Browse",
                 command = browseSource,
                 width = 60, height = 2,)
browse1.grid(column = 0,
             row = 1)


# Second label
select2 = Label(window,
                text = "Select Destination Directory:",
                width = 70, height = 2,
                fg = "blue",
                bg = "lightgray")
select2.grid(column = 0,
             row = 2)

browse2 = Button(window,
                 text = "Browse",
                 command = browseDest,
                 width = 60, height = 2,)
browse2.grid(column = 0,
             row = 3)


exitBtn = Button(window,
                 text = "Exit",
                 width = 20, height = 2,
                 command = exit)
exitBtn.grid(column = 0,
             row = 4,
             sticky = NW,
             padx = (32,32), pady = (10))


executeBtn = Button(window,
                    text = "Do the thing!",
                    width = 20, height = 2,
                    command = fileMover)
executeBtn.grid(column = 0,
                row = 4,
                sticky = NE,
                padx = (32,32), pady = (10))
