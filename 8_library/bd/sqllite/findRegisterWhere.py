import sqlite3

connection = sqlite3.connect("bdmovies.db")
cursor = connection.cursor()

sql = "SELECT * FROM PERSON WHERE lastName like 'perez'"
cursor.execute(sql)

list_person = cursor.fetchall()

for person in list_person:
    print(person)

connection.close()
