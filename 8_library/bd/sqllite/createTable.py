import sqlite3

connection = sqlite3.connect("bdmovies.db")
cursor = connection.cursor()

sql = "CREATE TABLE PERSON(name TEXT, lastName TEXT)"
cursor.execute(sql)
connection.commit()

connection.close()
