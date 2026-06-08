import mysql.connector as mycon
mydb=mycon.connect(host='localhost',
                   database="xii",
                   user='root',
                   passwd='0000',charset="utf8")#Enter the SQL Password in place of 0000
mycursor=mydb.cursor()
x=int(input("enter no. of people : "))
for i in range(x):
    print("--------------------------------------------------------------------------------------------------------------------------------------")
    print( )
    print("Enter your Details :-")
    a=input("Enter your Name : ")
    b=int(input("Enter your Voter_id: "))
    c=int(input("Enter your Passcode : "))
    print("--------------------------------------------------------Details saves-----------------------------------------------------------")
    st="INSERT into voter_list values('{}','{}','{}')".format(a,c,b)
    mycursor.execute(st)
    mydb.commit()
    print("--------------------------------------------------------------------------------------------------------------------------------------")
    
