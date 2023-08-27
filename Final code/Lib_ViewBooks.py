#MODULE TO VIEW TABLE BOOKS 

from tabulate import tabulate
import mysql.connector

mydb = mysql.connector.connect(host = "localhost",\
                                                       user = "root",\
                                                       password = "password",\
                                                       database = "Library")
mycursor = mydb.cursor()

def ViewBooks():
    mycursor.execute("SELECT * FROM BOOKS;")
    data = []
    print("Book Details".center(100))
    for i in mycursor:
        data =data + [list(i)]
    head = ["Book ID","Book Name","Author","Copies","Available"]
    print(tabulate(data,headers=head,tablefmt="fancy_grid").center(100))




