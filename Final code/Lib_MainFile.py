#MAIN MODULE
import Lib_ViewBooks as VB
import Lib_ViewIssued as IB
import Lib_AddBooks as AB
import Lib_ReturnBooks as RB
import Lib_DeleteBooks as DB
import time

print("*"*100)
print( )
print("WELCOME".center(100))
print("TO".center(100))
print("KR MANGALAM LIBRARY".center(100))
print( )
print( )
print("*"*100)
print( )
a = input("\t\t\tENTER USER ID = ")
print( )
b = input("\t\t\tPASSWORD = ")
print( )

ch='y'
def menu() :
    while ( ch=='y' ):
        print("*"*100)
        print( )
        print("MAIN MENU".center(100))
        print( )
        print("1. View Books Table".center(100))
        print( )
        print("2. View Issued Books".center(100))
        print( )
        print("3. Add Books Data".center(100))
        print( )
        print("4. Returned Books Update".center(100))
        print( )
        print("5. Delete Books Data".center(100))
        print( )
        print("6. Exit From Menu".center(100))
        print( )
        print("*"*100)
        c= int(input("\t\t\tEnter your Choice =  "))
        print("*"*100)
        if c==1:
            VB.ViewBooks()
        elif c==2 :
            IB.ViewIssued()
        elif c==3 :
            AB.AddBooks()
        elif c==4 :
            RB.Available()
            RB.Returned()
        elif c==5 :
            DB.DeleteData()
        elif c==6 :
            print("***** EXITING THE PROGRAM IN FIVE SECONDS*****".center(100))
            time.sleep(5)
            break
        else :
            print("Please Check Your Input".center(100))
        print("*"*100)

if a=='Admin' and  b=='1212':
    menu()

    
    
