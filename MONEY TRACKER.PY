# OUR FAV MONEY TRACKER 

print("                          WELCOME TO OUR MONEY TRACKER APP ")

print("\n                           =================MAIN MENU=================    ")
print("\n 1] ADD EXPENSE")
print("\n 2] VIEW ALL EXPENSES")
print("\n 3] VIEW TOTAL SPENDINGS")
print("\n 4]EXIT ")
print("\n                            ====================================== ")

#MAIN MENU
t = 0
c = int(input("ENTER YOUR CHOICE (1-4) : "))


if (c==1):
    e = int(input("ADD AMOUNT OF EXPENSE (IN RUPEES) : "))
    f = str(input("ENTER THE PURPOSE OF EXPENSE :  "))
    d = str(input("ENTER DATE (DD-MM-YYYY) : "))
    t = t + e
    menu = int(input("\n PRESS 1 TO EXIT OR PRESS 2 TO CONTINUE : "))
    if (menu==1):
            print("=========================TASK ENDED=============================== ")
    
    if (menu==2):
            print("=========================MENU======================================")
            print("\n 1] ADD EXPENSE")
            print("\n 2] VIEW ALL EXPENSES")
            print("\n 3] VIEW TOTAL SPENDINGS")
            print("\n 4]EXIT ")
            c = int(input("ENTER YOUR CHOICE (1-4) : "))
    
            if (c==1):
                e = int(input("ADD AMOUNT OF EXPENSE (IN RUPEES) : "))
                f = str(input("ENTER THE PURPOSE OF EXPENSE :  "))
                d = str(input("ENTER DATE (DD-MM-YYYY) : "))
                t = t + e
                menu = int(input("\n PRESS 1 TO EXIT OR PRESS 2 TO CONTINUE : "))
                if (menu==1):
                     print("=========================TASK ENDED=============================== ")
                    
                if (menu==2):
                    print("=========================MENU======================================")
                    print("\n 1] ADD EXPENSE")
                    print("\n 2] VIEW ALL EXPENSES")
                    print("\n 3] VIEW TOTAL SPENDINGS")
                    print("\n 4]EXIT ")
                    c = int(input("ENTER YOUR CHOICE (1-4) : "))
                    
                    if (c==1):
                        e = int(input("ADD AMOUNT OF EXPENSE (IN RUPEES) : "))
                        f = str(input("ENTER THE PURPOSE OF EXPENSE :  "))
                        d = str(input("ENTER DATE (DD-MM-YYYY) : "))
                        t = t + e

                    if(c==2):
                        print("ALL EXPENSES :- ")
                        print((e) , ":" , f ," ON DATE : " , d )
                        print("\n ============= END OF EXPENSES ================")
            
            if(c==2):
                print("ALL EXPENSES :- ")
                print((e) , ":" , f ," ON DATE : " , d )
                print("\n ============= END OF EXPENSES ================")
    

if (c==2):
    print(" NO EXPENSES TILL NOW !!! ")
    menu = int(input("\n PRESS 1 TO EXIT OR PRESS 2 TO CONTINUE : "))
    if (menu==1):
        print("=========================TASK ENDED=============================== ")

    if (menu==2):
        print("=========================MENU======================================")
        print("\n 1] ADD EXPENSE")
        print("\n 2] VIEW ALL EXPENSES")
        print("\n 3] VIEW TOTAL SPENDINGS")
        print("\n 4]EXIT ")

        c = int(input("ENTER YOUR CHOICE (1-4) : "))

    
        if (c==1):
            e = int(input("ADD AMOUNT OF EXPENSE (IN RUPEES) : "))
            f = str(input("ENTER THE PURPOSE OF EXPENSE :  "))
            d = str(input("ENTER DATE (DD-MM-YYYY) : "))
            t = t + e
            menu = int(input("\n PRESS 1 TO EXIT OR PRESS 2 TO CONTINUE : "))
            if (menu==1):
                print("=========================TASK ENDED=============================== ")
                                
            if (menu==2):
                print("=========================MENU======================================")
                print("\n 1] ADD EXPENSE")
                print("\n 2] VIEW ALL EXPENSES")
                print("\n 3] VIEW TOTAL SPENDINGS")
                print("\n 4]EXIT ")
                c = int(input("ENTER YOUR CHOICE (1-4) : "))

        if(c==2):
            print("ALL EXPENSES :- ")
            print(" NO EXPENSES TILL NOW !!! ")
    

if(c==4):
        print("\n                 =====================THANK YOU=======================")

if(c==3):
     print(" TOTAL SPENDINGS(IN RUPEES) :- ")
     print( "TODAY :  " , t ,"RUPEES" )





