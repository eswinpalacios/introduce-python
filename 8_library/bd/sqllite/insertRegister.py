import sqlite3

connection = sqlite3.connect("bdmovies.db")
cursor = connection.cursor()

sql = "INSERT INTO PERSON VALUES('Juan', 'Perez') "
cursor.execute(sql)

connection.commit()
connection.close()
