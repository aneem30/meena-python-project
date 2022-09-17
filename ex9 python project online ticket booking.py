import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="queen30",
    database="python_batch"
)    

mycursor=mydb.cursor()
def insert_data(booker_name,how_many_members,seat_num,travels_name,place_name):
    mycursor=mydb.cursor()
    sql="insert into online_ticket_booking(booker_name,how_many_members,seat_num,travels_name,place_name) values (%s,%s,%s,%s,%s)"
    val=(booker_name,how_many_members,seat_num,travels_name,place_name)
    mycursor.execute(sql,val)
    mydb.commit()
    print("data inserted successfully")
def view_data():
    mycursor.execute("select*from online_ticket_booking")  
    result=mycursor.fetchall()
    for i in result:
     print(i) 
user= int(input("enter your number:"))
if user==1:
    booker_name=input("enter your name:")
    how_many_members=int(input("how many members:"))
    seat_num=int(input("enter your seat num:"))
    travels_name=input("enter your travel name:")
    place_name=input("enter your place name:")
    insert_data(booker_name,how_many_members,seat_num,travels_name,place_name)
elif user==2:
    view_data()    
