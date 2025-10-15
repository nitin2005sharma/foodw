
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="Nitin@200527" ,database = "fdatabase")

mycursor = mydb.cursor()
query="SHOW FULL TABLES IN fdatabaseB WHERE TABLE_TYPE LIKE 'VIEW';"
mycursor.execute(query)
myresult = mycursor.fetchall()
print('Views are')
for x in myresult:
   print(x)
print()

