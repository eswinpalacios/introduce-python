import sqlite3

connection = sqlite3.connect("bdmovies.db")
cursor = connection.cursor()

list_person = [('Marco', 'Gonzales'), ('Maria', 'Fuentes')]
cursor.executemany("INSERT INTO PERSON VALUES(?, ?)", list_person)

connection.commit()
connection.close()
