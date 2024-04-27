import sqlite3
import unittest

# function that prompts user to create a new account
def create_account():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    balance = 0
    conn = sqlite3.connect('geek.db')
    cursor = conn.cursor()
    cursor.execute(
        '''INSERT INTO BANKS (USERNAME, PASSWORD, BALANCE) 
        VALUES (?, ?, ?)''', (username, password, balance))
    conn.commit()
    conn.close()
    print("Account created successfully!")
    menu()
# function that prompts user to login
def login():
  account_number = input("Enter your account number: ")
  pin = input("Enter your PIN: ")
  conn = sqlite3.connect('geek.db')
  cursor = conn.cursor()
  cursor.execute(
    '''INSERT INTO LOGIN (ACCOUNTNUMBER, PIN)
  VALUES (?, ?)''', (account_number, pin))
  conn.commit()
  conn.close()
  
  print("Login successful!")
  menu()
# function that displays menu
def menu():
    print("Welcome")
    
    print("1. Create Account")
    print("2 Delete Account")
    print("3. Check Balance")
    print("4. Deposit")
    print("5. Withdraw")
    print("6. Change username")
    print("7. Change password")
    print("8. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        create_account()
    if choice == "2":
        delete()
    if  choice == "3":
        check_balance()
    if choice == "4":
        deposit()
    if choice == "5":
        withdraw()

    if choice == "6":
      change_username()
    if choice == "7":
      change_password()
    if choice == "8":
      exit()
    else:
      print("Please pick a valid option")

# function that deletes account
def delete():
  username = input("Enter your username: ")
  password = input("Enter your password: ")
  conn = sqlite3.connect('geek.db')
  cursor = conn.cursor()
  cursor.execute('''DELETE FROM BANKS WHERE USERNAME = ? AND PASSWORD = ?'''
                 , (username, password))
  conn.commit()
  conn.close()
  print("Account deleted successfully!")
  menu()
# funtion that checks balance
def check_balance():
  username = input("Enter your username: ")
  password = input("Enter your password: ")
  conn = sqlite3.connect('geek.db')
  cursor = conn.cursor()
  cursor.execute('''SELECT BALANCE FROM BANKS WHERE USERNAME = ? AND PASSWORD = ?'''
                 , (username, password))
  balance = cursor.fetchone()
  conn.close()
  print("Your balance is: ", balance)
  menu()
# function that deposits money
def deposit():
  username = input("Enter your username: ")
  password = input("Enter your password: ")
  amount = float(input("Enter the amount to deposit: "))
  conn = sqlite3.connect('geek.db')
  cursor = conn.cursor()
  cursor.execute('''UPDATE BANKS SET  
  BALANCE = BALANCE + ? WHERE USERNAME = ? AND PASSWORD = ?'''
                 , (amount, username, password))
  conn.commit()
  conn.close()
  print("Deposit successful!")
  menu()
# function that withdraws money
def withdraw():
  username = input("Enter your username: ")
  password = input("Enter your password: ")
  amount = float(input("Enter the amount to withdraw: "))
  conn = sqlite3.connect('geek.db')
  cursor = conn.cursor()
  cursor.execute('''UPDATE BANKS SET  
  BALANCE = BALANCE - ? WHERE USERNAME = ? AND PASSWORD = ?'''
                 , (amount, username, password))
  conn.commit()
  conn.close()
  print("Withdrawal successful!")
  menu()
# function that changes account username
def change_username():
  old_username = input("Enter your old username: ")
  new_username = input("Enter your new username: ")
  password = input("Enter your password: ")
  conn = sqlite3.connect('geek.db')
  cursor = conn.cursor()
  cursor.execute('''UPDATE BANKS SET  
  USERNAME = ? WHERE USERNAME = ? AND PASSWORD = ?'''
                 , (new_username, old_username, password))
  conn.commit()
  conn.close()
  print("Username changed successfully!")
  menu()

# function that changes password
def change_password():
  username = input("Enter your username: ")
  old_password = input("Enter your old password: ")
  new_password = input("Enter your new password: ")
  conn = sqlite3.connect('geek.db')
  cursor = conn.cursor()
  cursor.execute('''UPDATE BANKS SET  
  PASSWORD = ? WHERE USERNAME = ? AND PASSWORD = ?'''
                 , (new_password, username, old_password))
  conn.commit()
  conn.close()
  menu()

# exits program
def exit():
  print("Thank you for using our banking system!")