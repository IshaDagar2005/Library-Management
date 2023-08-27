#MODULE TO DELETE ANY BOOK FROM THE DATABASE 

import mysql.connector
mydb = mysql.connector.connect(host = "localhost",\
                                                       user = "root",\
                                                       password = "password",\
                                                       database = "Library")
mycursor =mydb.cursor()

def DeleteData():
    bookid= input("\t\t\tEnter the BookID of the Book to be Deleted : ")
    mycursor.execute("DELETE from Books WHERE BookID ="+bookid+";")
    mydb.commit()
    print("Book Successfully deleted from the Database".center(100))

