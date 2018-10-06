import requests
import re
from bs4 import BeautifulSoup
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="14521452",
    database='cars'
)
mycursor = mydb.cursor()
a="hjkh"
b="hjkg"
SQLInsertCmd = """INSERT INTO carinfo(Usage,Price) VALUES ((%s,%s))"""  % (a,b)
mycursor.execute(SQLInsertCmd)
mycursor.execute("INSERT INTO carinfo""(Usage, Price)"" VALUES (%s, %s)",(a,b))
brand=input("Which car brand are you interested in?")
response = requests.get('https://bama.ir/car/%s'% brand)
soup = BeautifulSoup(response.text, 'html.parser')
database = "cars"

insert_data = ("INSERT INTO carinfo "
                   "(Usage, Price) "
                   "VALUES (%s, %s)")

mycursor.execute(insert_data,(a, b))



