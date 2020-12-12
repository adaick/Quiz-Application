import sqlite3

with sqlite3.connect("quizdatabase.db")as db:
    cursor = db.cursor()

cursor.execute("""DELETE FROM quizzes""")
db.commit()

cursor.execute("""
INSERT INTO quizzes(quizName)
VALUES("Python_basic"),("Python_datatypes"),("Miscellaneous");
""")
db.commit()

cursor.execute("""DELETE FROM questions""")
db.commit()

cursor.execute("""
INSERT INTO questions(quizID,question,option1,option2,option3,option4,answer)
VALUES("1","What is the name of the Python element used to store groups or segments of text?","String","Variable","Constant","Operator","1"),
("1","Strings are defined with quotes in either ____ or ____ form","Open or Closed","Single or Double","Straight or Squiggly","Front or Back","2"),
("1","What is the full name of the Python tool that is used to match patterns in text","Code Handler","Executor","Logical Operator","Regular Expression","4"),

("2","what is the type of type(range(5))","range","list","none","int","1"),
("2","What is the data type of print(type(10))","int","float","integer","none","3"),
("2","What is the result of print(type({}) is set)","True","Error","False","none","1"),

("3","What is the return type of function id","float","bool","dict","int","4"),
("3","All keywords in Python are in","UPPER CASE","lower case","Capitalized","None of the mention","4"),
("3","Which of the following data types is not supported in python","String","Slice","List","Numbers","2");
""")
db.commit()


 
 
 
 
 
 

 
