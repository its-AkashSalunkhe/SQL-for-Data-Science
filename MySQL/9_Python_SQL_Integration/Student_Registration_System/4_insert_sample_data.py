# We are inserting the values in database that we created - "intershipdb" and table "student"



import mysql.connector

conn = mysql.connector.connect(host = 'localhost',user='root',password='5703',database='internshipdb')

mycursor = conn.cursor()

sql = 'insert into student (name,branch,id) values(%s,%s,%s)'
#val = ('john','cse',56)

# if user want to create multiple value then you can creat list 
val = [('john','cse','56'),('mike','IT','78'),('tyson','me','80')]
#mycursor.execute(sql,val)
mycursor.executemany(sql,val)
conn.commit()
print(mycursor.rowcount,'record inserted')