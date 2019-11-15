import random
import string
import sqlite3


connection = sqlite3.connect("Data.db")
cursor = connection.cursor()
table = "CREATE TABLE SimData(ID TEXT PRIMARY KEY UNIQUE, Arrival INTEGER, Duration INTEGER)"
cursor.execute(table)
connection.commit()

global wordID
global arrival
global duration
for x in range(100):
    def randomID(stringLength=6):
        characters = string.ascii_letters + string.digits + "@_#*-&"
        return ''.join(random.choice(characters) for i in range(stringLength))
    wordID = randomID()

    arrival = random.randint(1, 100)

    duration = round(random.uniform(0, 1), 2)
    cursor.execute("INSERT INTO SimData(ID, Arrival, Duration) VALUES(?, ?, ?)", (wordID, arrival, duration))
    connection.commit()

connection.close()
