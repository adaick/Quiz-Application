import sqlite3

with sqlite3.connect("quizdatabase.db")as db:
    cursor = db.cursor()

def showScores(user):
    query = ("""SELECT quizzes.quizName, scores.score, user.Fname
    FROM user INNER JOIN (quizzes INNER JOIN scores ON quizzes.quizID = scores.quizID) ON user.userID = scores.userID
    WHERE (((user.userID)=?));""")
    cursor.execute(query, [(user)])
    results = cursor.fetchall()
    #print(results)
    for line in results:
        print(line[2]," " + "Your score from quiz" + " "+ str(line[0]),"is" + " "+ str(line[1]) + "%")
        #print(line)
        print("")