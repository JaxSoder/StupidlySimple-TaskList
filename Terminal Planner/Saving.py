import sqlite3

from TaskHandler import *

def CreateTaskServer(id, task_text, status):

    conn = sqlite3.connect('tasks.db')

    conn.execute("INSERT INTO Tasks (ID, Text, Status) \
      VALUES ("+str(id)+", '"+task_text+"', "+str(status)+")")
    conn.commit()
    conn.close()

def DeleteTaskServer(id):
    conn = sqlite3.connect('tasks.db')

    conn.execute("DELETE from Tasks where ID = "+str(id)+"")
    conn.commit()
    conn.close()


def MarkTaskServer(id, status):
    conn = sqlite3.connect('tasks.db')

    conn.execute("UPDATE Tasks set Status = "+str(status)+" where ID = "+str(id)+"")
    conn.commit()
    conn.close()


def LoadDatabase(Task_List):
    conn = sqlite3.connect('tasks.db')

    cursor = conn.execute("SELECT ID, Text, Status from Tasks")
    for row in cursor:
        Task_List.append(Task(row[1], row[2]))
        
    conn.close()


def UpdateServerData(Task_List):
    DeleteAllRows() 

    for index, task in enumerate(Task_List): 
        if task.status == True:
            CreateTaskServer(index, task.text, 1)
        else:
            CreateTaskServer(index, task.text, 0)


def DeleteAllRows():
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()

    # delete all rows from table
    c.execute('DELETE FROM Tasks;',)

    conn.commit()
    conn.close()