import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="queen30",
    database="python_batch"

)

mycursor=mydb.cursor()
sql="insert into atm_machine (ac_holder_name,total_balance,enter_your_pin,withdraw_amount,balace) values (%s,%s,%s,%s,%s)"
val=("meena",50000,1234,500,45000)
val=("priya",30000,3469,500,25000)
val=("usha",70000,4657,500,65000)
mycursor.execute(sql,val)
mydb.commit()
print("data inserted successfully")
def view_data():
    mycursor.execute("select * from atm_machine")
    result=mycursor.fetchall()
    for i in result:
        print(i)
user=int(input("enter your number:"))
if user==1:
  view_data()              

 

 