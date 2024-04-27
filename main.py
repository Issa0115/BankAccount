import sqlite3 # import sqlite3 library

from functions import login # import login function from functions.py

import tkinter
from tkinter import *
root = Tk()
w = Label(root, text='GeeksForGeeks.org!')
w.pack()
root.mainloop()

m.mainloop()

# Connecting to sqlite
conn = sqlite3.connect('geek.db') 

# Creating a cursor object using the
# cursor() method
cursor = conn.cursor()

# Creating table
table = """CREATE TABLE IF NOT EXISTS BANKS
(USERNAME VARCHAR(255), PASSWORD VARCHAR(255), 
BALANCE INT)
"""
cursor.execute(table)

# Queries to INSERT records.

#creating a second table for login
table2 = """CREATE TABLE IF NOT EXISTS LOGIN
(ACCOUNTNUMBER INT, PIN INT)"""

cursor.execute(table2)



# Display data inserted
login()




# Commit your changes in
# the database
conn.commit()

# Closing the connection
conn.close()
