#MODULE TO VIEW THE LIST OF BOOKS THAT ARE ISSUED

from tabulate import tabulate
import mysql.connector

mydb = mysql.connector.connect(host = "localhost",\
                                                       user = "root",\
                                                       password = "password",\
                                                       database = "Library")
mycursor = mydb.cursor()

def ViewIssued():
    mycursor.execute("SELECT * FROM ISSUED;")
    data = []
    print("Issued Books Details".center(100))
    for i in mycursor:
        data =data + [list(i)]
    head = ["Book ID","Book Name","Author","Issued To","Issued Date","Returned"]
    print(tabulate(data,headers=head,tablefmt="fancy_grid").center(100))
