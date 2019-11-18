import sqlite3
import random

connection = sqlite3.connect("Data.db")
cursor = connection.cursor()

tableData = "SELECT * FROM SimData ORDER BY Arrival"
tableWord = "SELECT ID FROM SimData ORDER BY Arrival"
tableArrival = "SELECT Arrival FROM SimData ORDER BY Arrival"
tableDuration = "SELECT Duration FROM SimData ORDER BY Arrival"

cursor.execute(tableData)
data = cursor.fetchall()

cursor.execute(tableWord)
word = cursor.fetchall()

cursor.execute(tableArrival)
arrivalTime = cursor.fetchall()

cursor.execute(tableDuration)
taskDuration = cursor.fetchall()


'''for d in word:
    c = str(d).strip("(),''")
    print(c)'''

'''for s in arrivalTime:
    t = str(s).strip("(),")
    print(t)'''

'''for b in taskDuration:
    e = str(b).strip("(),")
    print(e)'''

for x in range(100):
    #ran = round(random.uniform(0, 1), 2)
    #ran = round(random.random(), 2)
    ran = round(random.expovariate(1), 2)
    print(ran)


# length = len(data)
"""print(word)
print(arrivalTime)
print(taskDuration)"""


'''for a in data:
    print(a)'''

