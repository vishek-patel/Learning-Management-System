                                                         #library management system
import mysql.connector as a
con = a.connect (host="localhost",user="root",passwd="1234",database="library")


def addbook():
    bn = input("ENTER BOOK NAME : ")
    c = input("ENTER BOOK CODE : ")
    t = input("TOTAL BOOKS : ")
    s = input("ENTER SUBJECT : ")
    data = (bn,c,t,s)
    sql = "insert into books values(%s,%s,%s,%s)"
    c = con.cursor()
    c.execute(sql,data)
    con.commit()
    print(">-----------------------------------------------------------------------------------------------------------------------<")
    print("Data Entered Successfully")
    main()

def issueb():
    n = input("ENTER NAME : ")
    r = input("ENTER REG NO : ")
    co = input("ENTER BOOK CODE : ")
    d = input("ENTER DATE : ")
    a = "insert into issue values(%s,%s,%s,%s)"
    data = (n,r,co,d)
    c = con.cursor()
    c.execute(a,data)
    con.commit()
    print(">-----------------------------------------------------------------------------------------------------------------------<")
    print("Book issued to : ",n)
    bookup(co,-1)

def submitb():
    n = input("ENTER NAME : ")
    r = input("ENTER REG NO : ")
    co = input("ENTER BOOK CODE : ")
    d = input("ENTER DATE : ")
    a = "insert into submit values(%s,%s,%s,%s)"
    data = (n,r,co,d)
    c = con.cursor()
    c.execute(a,data)
    con.commit()
    print(">-----------------------------------------------------------------------------------------------------------------------<")
    print("Book submited by : ",n)
    bookup(co,1)

def bookup(co,u):
    a = "select total from books where bcode =%s"
    data = (co,)
    c = con.cursor()
    c.execute(a,data)
    myresult = c.fetchone()
    t = myresult[0]+ u
    sql = "update books set total =%s where bcode =%s"
    d = (t,co)
    c.execute(sql,d)
    con.commit()
    main()
    
def dbook():
    ac = input("ENTER BOOK CODE : ")
    a = "delete from books where bcode = %s"
    data = (ac,)
    c = con.cursor()
    c.execute(a,data)
    con.commit()
    print("BOOKS DELETED SUCESSFULLY")
    main()

def dispbook():
    mycursor = con.cursor()
    mycursor.execute("select * from books")
    for i in mycursor:
        print(" BOOKNAME : ",i[0], "         BCODE : ",i[1], "      TOTAL : ",i[2], "         SUBJECT : ",i[3], "\n")

        
    main()


def  main():
    print("""                                                      
                                                            LIBRARY MANAGER
                                                            
          1. ADD BOOK
          2. ISSUE BOOK
          3. SUBMIT BOOK
          4. DELETE BOOK
          5. DISPLAY BOOK
          6. EXIT FUNCTION
          """)
    choice = input("Enter Task No : ")
    print(">-----------------------------------------------------------------------------------------------------------------------<")
    if(choice =='1'):
        addbook()
    elif(choice=='2'):
        issueb()
    elif(choice=='3'):
        submitb()
    elif(choice=='4'):
        dbook()
    elif(choice=='5'):
        dispbook()
    elif(choice=='6'):
        print(">---------------------------------------------------------------------------------------------------------------------<")
    else :
        print("wrong choice")
        main()

        


def pswd():
    ps = input("ENTER PASSWORD")
    if ps == "1234":
        main()
    else:
        print("WRONG PASSWORD")
        pswd()

pswd()
