#MODULE TO ADD BOOKS IN THE DATABASE
import mysql.connector
mydb = mysql.connector.connect(host = "localhost",\
                                                       user = "root",\
                                                       password = "password",\
                                                       database = "Library")
mycursor = mydb.cursor()

def AddBooks():
    a = input("\t\t\t   Enter 'New' To Add A New Book\n\t\tTo Add New Copies For A Pre-exicting Book Enter 'Existing'\n\t\t\t\t    ")
    if a == 'New':
        print()
        print("Enter Data of the New Book".center(100))
        print()
        ID = input("\t\t\t\tBook ID : ")
        Name = input("\t\t\t\tBook Name : ")
        Author = input("\t\t\t\tAuthor : ")
        Copies = input("\t\t\t\tNumber of Copies : ")

        mycursor.execute("INSERT INTO BOOKS VALUES("+ID+",'"+Name+"','"+Author+"',"+Copies+",'Yes');")
        mydb.commit()
        
        print()
        print("Data Entered Successfully".center(100))
        
    elif a == 'Existing':
        Exist_Name=input("\t\t Enter The Name Of The Pre_existing Book : ")
        New_Copies = input("\t\t Enter The Number Of New Copies Added : ")
        mycursor.execute("SELECT Copies FROM Books WHERE BookName = '"+Exist_Name+"';")
        for i in mycursor:
            Exist_Copies = i[0]
        Total_Copies = str(Exist_Copies+int(New_Copies))
        mycursor.execute("UPDATE BOOKS SET Copies ="+Total_Copies+" WHERE BookName = '"+Exist_Name+"';")
        mydb.commit()

        print("Data Entered Successfully".center(100))
    else :
        print("Invalid Input".center(100))
        print("Try Again".center(100))


