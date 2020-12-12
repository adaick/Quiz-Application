import time
import sqlite3


def user_login():
    for i in range(1, 3):
        username = input("Enter your username:- ")
        password = input("Enter your password:- ")

        with sqlite3.connect("quizdatabase.db")as db:
            cursor = db.cursor()
        check = ("SELECT * FROM user WHERE username = ? AND password = ?")
        cursor.execute(check, [username, password])
        valid_user = cursor.fetchall()

        if valid_user:
            for j in valid_user:
                print("Welcome "+j[2])
                start = input("Are you ready to see the available option? Y/N ")
            return start, j[0]

        if i == 2:
            print("Sorry, too many failed login attempts, please wait 10 seconds ")
            time.sleep(10)
            i -= 1

        else:
            start = input("Sorry but your username or password is incorrect, try again? Y/N ")
            if start == "N":
                return start
            else:
                start = user_login()


def new_user():
    print("Add new user")
    time.sleep(1)

    #  checking username isn't already in use
    flag = False
    while not flag:
        username = input("Please enter your preferred username ")
        with sqlite3.connect("quizdatabase.db")as db:
            cursor = db.cursor()
        clash = ("SELECT * FROM user WHERE username = ?")
        
        cursor.execute(clash, [username])
        if cursor.fetchall():
            print("Sorry, this username is already taken, please try another one :( ")
        else:
            flag = True

    fname = input("Please enter your first name:- ")
    lname = input("Please enter your lastname:- ")

    # checking password length and error
    password_flag = False
    while not password_flag:
        password1 = input("Please enter your password:- ")
        password2 = input("Please re-enter your password:- ")

        if password1 != password2:
            print("Sorry but your passwords dont match :(")

        elif len(password1) < 6:
            print("Sorry but your password is too short it must be 6 characters :(")

        else:
            password = password1
            password_flag = True

    add_user = """INSERT INTO user(username, Fname, Lname, password)
    values(?,?,?,?)"""
    cursor.execute(add_user, [(username),(fname),(lname),(password)])
    db.commit()
    print("Thank you for successfully creating a user account :)")
