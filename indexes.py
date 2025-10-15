import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="Nitin@200527" ,database = "fdatabase")

mycursor = mydb.cursor()
query="SHOW INDEX FROM fdatabase.Contains;"
mycursor.execute(query)
myresult = mycursor.fetchall()
print('Indexes for Contains: ')
for x in myresult:
   print(x)
print()
query="SHOW INDEX FROM fdatabase.Customer; "
mycursor.execute(query)
myresult = mycursor.fetchall()
print('Indexes for Customer:')
for x in myresult:
   print(x)
print()
query="SHOW INDEX FROM fdatabase.DeliveryWorker; "
mycursor.execute(query)
myresult = mycursor.fetchall()
print('Indexes for DeliveryWorker:')
for x in myresult:
   print(x)
print()
query="SHOW INDEX FROM fdatabase.Donation; "
mycursor.execute(query)
myresult = mycursor.fetchall()
print('Indexes for Donation:')
for x in myresult:
   print(x)
print()
query="SHOW INDEX FROM fdatabase.Donor; "
mycursor.execute(query)
myresult = mycursor.fetchall()
print('Indexes for Donor:')
for x in myresult:
   print(x)
print()
query="SHOW INDEX FROM fdatabase.Food; "
mycursor.execute(query)
myresult = mycursor.fetchall()
print('Indexes for Food:')
for x in myresult:
   print(x)
print()
query="SHOW INDEX FROM fdatabase.Management; "
mycursor.execute(query)
myresult = mycursor.fetchall()
print('Indexes for Management:')
for x in myresult:
   print(x)
print()
query="SHOW INDEX FROM fdatabase.Orders; "
mycursor.execute(query)
myresult = mycursor.fetchall()
print('Indexes for Orders:')
for x in myresult:
   print(x)
print()
query="SHOW INDEX FROM fdatabase.Rates; "
mycursor.execute(query)
myresult = mycursor.fetchall()
print('Indexes for Rates:')
for x in myresult:
   print(x)
print()
query="SHOW INDEX FROM fdatabase.Receiver; "
mycursor.execute(query)
myresult = mycursor.fetchall()
print('Indexes for Receiver:')
for x in myresult:
   print(x)
print()
query="SHOW INDEX FROM fdatabase.Restaurant; "
mycursor.execute(query)
myresult = mycursor.fetchall()
print('Indexes for Restaurant:')
for x in myresult:
   print(x)