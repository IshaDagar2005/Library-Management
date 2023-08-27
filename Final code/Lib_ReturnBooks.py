#MODULE TO UPDATE TABLES WHEN A BOOK IS RETURNED

import mysql.connector
mydb = mysql.connector.connect(host = "localhost",\
                                                       user = "root",\
                                                       password = "password",\
                                                       database = "Library")
mycursor=mydb.cursor()

def Available():
    bookid= input("\t\t\tEnter the BookID of Book(for data update) :  ")
    mycursor.execute("UPDATE Books SET Available='Yes' WHERE BookID="+bookid+";")
    print()
    print("Availability Updated to 'YES' Successfully".center(100))
    mydb.commit()
    
def Returned():
    bookid= input("\t\t\tEnter the BookID of Book(for returning update) :  ")
    mycursor.execute("UPDATE ISSUED SET Returned='Yes' WHERE BookID="+bookid+";")
    print()
    print("Return Updated to 'YES' Successfully".center(100))
    mydb.commit()
    
