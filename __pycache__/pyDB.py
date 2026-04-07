import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="258036bm,"
)

mycursor=mydb.cursor()

mycursor.execute("show databases")

for x in  mycursor:
    print(x)