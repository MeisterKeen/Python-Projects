# 
# Author: KEEN LITTLE
#
# Date: 29 March 2021
# 
# Assignment Step 214, Python Course
#   The Tech Academy Software Development Bootcamp
# 
# Purpose: to practice with python3 and sqlite3, showing how SQL queries can be
#   written and automated with Python.
#
################################################################################


import sqlite3

fileList = ('information.docx', 'hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')
            # Here are the file names that we're pulling into the database.


def createTable():
    conn = sqlite3.connect('pysql.db')
    with conn:
        cur = conn.cursor() # Creating a database with two fields:
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_textFiles( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fileName VARCHAR(50) \
            )") # We have a primary key and a varchar (string) for the names.
        conn.commit()
    conn.close()

"""
txtFileList = ()

def sortFiles(): # I'm just gonna grab the files I want
    for i in fileList:
	if i.endswith('.txt'):
	    txtFileList.append(i) # And dump 'em into a new list! Easier.
""" # Better idea: sort this with an if statement when I populate the table


def filesToTable(): 
    conn = sqlite3.connect('pysql.db')
    for item in fileList: # Iterating through the tuple,
        if item.endswith('.txt'): # Here we grab only the .txt files
            with conn: 
                cur = conn.cursor()
                cur.execute("INSERT INTO tbl_textFiles (col_fileName) VALUES (?)", (item,))
                print(item)
                conn.commit()
    conn.close()



if __name__ == "__main__":

    createTable()
#    sortFiles()
    filesToTable()
    
