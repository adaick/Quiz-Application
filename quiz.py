import sqlite3


def quiz(quiz, user):
    with sqlite3.connect("quizdatabase.db")as db:
        cursor = db.cursor()

    score = 0
    Qnum = 0
    cursor.execute("SELECT * FROM questions WHERE quizID=?;", [(quiz)])
    questions = cursor.fetchall()

    for question in questions:
        topic = question[1]
        print("Q."  + question[2])
        print("\n 1. %s \n 2. %s \n 3. %s \n 4. %s \n" %(question[3], question[4], question[5], question[6]))
        choice = input("Choose your answer: ")
        if choice == question[7]:
            print("Correct")
            score += 1
            print("")
        else:
            print("Incorrect")
        
        Qnum += 1
        
		
		
		
		
		
		
		

    scorePercent = int((score/Qnum)*100)
    print("You scored %s percent" %scorePercent)
    print("")

    insertData = ("INSERT INTO scores(userID, score, quizID) VALUES(?,?,?);")
    cursor.execute(insertData, [(user), (scorePercent), (quiz)])
    db.commit()
