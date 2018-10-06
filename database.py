import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="14521452",
    database="employee"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE employeeinfo3(Name VARCHAR(255),Weight INTEGER(10),Height INTEGER(10) )")
sqlformula = "INSERT INTO employeeinfo3 (Name, Weight, Height) VALUES (%s,%s,%s)"
em1 = ("Amin",75,180)
mycursor.execute(sqlformula,em1)
em2 =("Mahdi",90,190)
mycursor.execute(sqlformula,em2)
em3 = ("Mohammad",75,175)
mycursor.execute(sqlformula,em3)
em4 = ("Ahmad",60,175)
mycursor.execute(sqlformula,em4)
em = [("Maryam",67,167),("Lida",81,164)]
mycursor.executemany(sqlformula,em)
mydb.commit()


mycursor.execute("SELECT * FROM employeeinfo3 ORDER BY Height DESC, Weight ASC ")

result = mycursor.fetchall()
for row in result:
    print (row)
