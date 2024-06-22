import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Adi@190605'
)


cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE User")
print("Done!!!")