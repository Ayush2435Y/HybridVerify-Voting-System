import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0000",#Enter the SQL Password in place of 0000
    database="xii",charset="utf8"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT COUNT(*) FROM voter_list")
result = mycursor.fetchone()
l=result[0]
mydb.close()
def sql(voter_id):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="0000",#Enter the SQL Password in place of 0000
        database="xii",charset="utf8"
    )
    mycursor = mydb.cursor()
    query = "SELECT Passcode FROM voter_list WHERE Voter_id = %s"
    mycursor.execute(query, (voter_id,))
    result = mycursor.fetchone()
    mydb.close()
    if result:
        return result[0]
    else:
        return 0
b=0
BJP=0
AJP=0
Congress=0
x=[]
for i in range(l):
    print("--------------------------------------------------------------------------------------------------------------------------------------")
    print( )
    print("Enter your Details :-")
    y=input("Enter  your name : ")
    for j in range(3):
       c=int(input("Enter your voter id : ")) 
       a=int(input("Enter your passcode : "))
       b=sql(c)
       print("--------------------------------------------------------------------------------------------------------------------------------------")
       if a==b: 
            if  c not in x:
                 print("--------------------------------------------------------Access Granted--------------------------------------------------------")
                 x.append(c)
                 print("--------------------------------------------------------------------------------------------------------------------------------------")
                 print('''The list of party : 
                           1) BJP
                           2) AJP
                           3) Congress''')
                 p=int(input("Select the party no. you want to vote : "))
                 if p==1:
                     BJP+=1
                     print("Your Vote have been Registered thank you for voting")
                     print("--------------------------------------------------------------------------------------------------------------------------------------")
                 elif p==2:
                     AJP+=1
                     print("Your Vote have been Registered thank you for voting")
                     print("--------------------------------------------------------------------------------------------------------------------------------------")
                 elif p==3:
                     Congress+=1
                     print("Your Vote have been Registered thank you for voting")
                     print("--------------------------------------------------------------------------------------------------------------------------------------")
                 else:
                     print("Invalid option: ")
            else:
                print("-------------------------------------------------------Repeating_Voter_ID------------------------------------------------------")
                print("--------------------------------------------------------------------------------------------------------------------------------------")
            break  
       else:
            print("--------------------------------------------------------Access Denied--------------------------------------------------------")
            print("--------------------------------------------------------Incorrect Ditails-------------------------------------------------------")
            print("--------------------------------------------------------------------------------------------------------------------------------------")
print( )
print("----------------------------------------------------Result of the Election-----------------------------------------------------")
print("BJP: ",BJP,"AJP: ",AJP,"Congress: ",Congress)
print("--------------------------------------------------------------------------------------------------------------------------------------")




