import time
import sqlite3
import userlogin


def admin_login():
    for i in range(1, 3):
        adminname = input("Enter your adminname:- ")
        password = input("Enter your password:- ")

        with sqlite3.connect("quizdatabase.db")as db:
            cursor = db.cursor()
        check = ("SELECT * FROM user WHERE adminname = ? AND password = ?")
        cursor.execute(check, [adminname, password])
        valid_admin = cursor.fetchall()

        if valid_admin:
            for j in valid_admin:
                print("Welcome "+j[2])
                start = input("Are you ready to see the available option? Y/N ")
            return start, j[0]

        if i == 2:
            print("Sorry, too many failed login attempts, please wait 10 seconds ")
            time.sleep(10)
            i -= 1

        else:
            start = input("Sorry but your adminname or password is incorrect, try again? Y/N ")
            if start == "N":
                return start
            else:
                start = admin_login()


def new_admin():
    print("Add new admin")
    time.sleep(1)

    #  checking username isn't already in use
    flag = False
    while not flag:
        adminname = input("Please enter your preferred adminname ")
        with sqlite3.connect("quizdatabase.db")as db:
            cursor = db.cursor()
        clash = ("SELECT * FROM user WHERE adminname = ?")
        
        cursor.execute(clash, [adminname])
        if cursor.fetchall():
            print("Sorry, this adminname is already taken, please try another one :( ")
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

    add_admin = """INSERT INTO admin(adminname, Fname, Lname, password)
    values(?,?,?,?)"""
    cursor.execute(add_admin, [(adminname),(fname),(lname),(password)])
    db.commit()
    print("Thank you for successfully creating a admin account :)")


def add_question(user):
    with sqlite3.connect("quizdatabase.db")as db:
            cursor = db.cursor()
            query = ("""SELECT user.username, user.Fname
            FROM user
            WHERE (((user.userID)=?));""")
            cursor.execute(query, [(user)])
            results = cursor.fetchall()
            
            for line in results:
                if line[0] == 'admin' or 'ADMIN' or 'Admin':
                    print('-------------ADD QUESTIONS--------------')
                    print("----------------------------------------")
                    quizID = input("""Enter quiz ID:\n 
                    1 - Python_basic
                    2 - Python_datatypes
                    3 - Miscellaneous
                    """)
                    question = input("Enter the question that you want to add:\n")
                    option1= input("Enter option 1: ")
                    option2= input("Enter option 2: ")
                    option3= input("Enter option 3: ")
                    option4= input("Enter option 4: ")
                    answer = int(input("Enter correct option number(1,2,3,4): "))
                    lvl = int(input(print("""Enter level of quiz you want to take \n
                    1 - Easy
                    2- Medium
                    3 - Hard
                    """)))
                    addquestion = """INSERT INTO questions(quizID,question,option1,option2,option3,option4,answer,level)
                    values(?,?,?,?,?,?,?,?) """
                    cursor.execute(addquestion, [(quizID),(question),(option1),(option2),(option3),(option4),(answer),(lvl)])
                    db.commit()
                    print("\n Questions added success fully.")
                else:
                    print("********")
                    print("YOU ARE NOT AUTHORISED TO PERFORM THIS ACTION")
                    print("********")


# def admin_display():
#     print("*****  YOU ARE ON THE ADMIN PAGE *****")