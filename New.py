import sqlite3
import re
import collections


''' Fetching the previously generated database. I've sorted the data by arrival time in my Select query itself, thus reducing the need to write extra lines of code to sort it after fetching.'''

connection = sqlite3.connect("Data.db")
cursor = connection.cursor()

tableData = "SELECT * FROM SimData ORDER BY Arrival"
tableWord = "SELECT ID FROM SimData ORDER BY Arrival"
tableArrival = "SELECT Arrival FROM SimData ORDER BY Arrival"
tableDuration = "SELECT Duration FROM SimData ORDER BY Arrival"


''' Saving the data of the columns into lists. '''

cursor.execute(tableData)
data = cursor.fetchall()

cursor.execute(tableWord)
word = cursor.fetchall()

cursor.execute(tableArrival)
arrivalTime = cursor.fetchall()

cursor.execute(tableDuration)
taskDuration = cursor.fetchall()


''' Function to strip the undesired characters such as '',() from a string and return a clean string. '''


def string_cleaner(my_string):

    my_list = my_string
    for d in my_list:
        clean_word = str(d).strip("(),''")
        return clean_word


processor_1 = ''
processor_2 = ''
processor_3 = ''

''' Class for the rest of my functions. '''


class Processor:

    def __init__(self, task_id, task_arrival, task_duration, task_index):
        self.task_id = task_id
        self.task_arrival = task_arrival
        self.task_duration = task_duration
        self.task_index = task_index
        self.finish_time = float(task_arrival) + float(task_duration)

    ''' Function to check the validity of the task id using regular expressions.'''
    def id_validator(self):

        pattern = re.compile("(?mx)^((?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])|(?=.*[a-z])(?=.*[A-Z])(?=.*[@_#*&-])|(?=.*[a-z])(?=.*[0-9])(?=.*[@_#*&-])|(?=.*[A-Z])(?=.*[0-9])(?=.*[@_#*&-])).{6,}$")

        chars = self.task_id

        if re.match(pattern, chars):

            return True
        else:
            return False

    ''' Function to define the processors. '''
    def processors(self):

        global processor_1
        global processor_2
        global processor_3

        if processor_1 is '':

            processor_1 = self.task_id
            finish_time_1 = self.finish_time
            print("** {} : Task {} assigned to processor 1.\n\n".format(self.task_arrival, self.task_id))
            return finish_time_1

        elif processor_2 is '':

            processor_2 = self.task_id
            finish_time_2 = self.finish_time
            print("** {} : Task {} assigned to processor 2.\n\n".format(self.task_arrival, self.task_id))
            return finish_time_2

        elif processor_3 is '':

            processor_3 = self.task_id
            finish_time_3 = self.finish_time
            print("** {} : Task {} assigned to processor 3.\n\n".format(self.task_arrival, self.task_id))
            return finish_time_3

        else:
            print("** Task {} on hold.".format(self.task_id))


''' Creating the empty double-ended queues.'''
id_queue = collections.deque()
arrival_queue = collections.deque()
duration_queue = collections.deque()


''' Inserting the 'cleaned' values from the lists of fetched data into the empty deques. '''
for each in word:
    id_queue.append(string_cleaner(each))

for arrival in arrivalTime:
    arrival_queue.append(string_cleaner(arrival))

for duration in taskDuration:
    duration_queue.append(string_cleaner(duration))

''' Initialisation of the system. '''
print("\n\n** SYSTEM INITIALISED**\n\n")
clock = 0

for each_task in id_queue:

    index = id_queue.index(each_task)
    each_process = Processor(id_queue[index], arrival_queue[index], duration_queue[index], index)

    clock = arrival_queue[index]

    print("** {} : Task {} with duration {} enters the system.".format(arrival_queue[index], each_task, duration_queue[index]))

    if each_process.id_validator() is False:

        print("** Task {} unfeasible and discarded.\n\n".format(each_task))
        # id_queue.popleft()

    else:

        print("** Task {} accepted.".format(each_task))
        print(each_process.processors())


'''print(id_queue)
print(id_queue.popleft())
print(id_queue)'''
