
from TaskHandler import *
from Saving import *

def UserInput(Task_List):
    print(" ")
    command = input("What Would you like to do: ")

    if "create" in command and len(command) == 6 or "c" in command and len(command) == 1:
        task_text = input("Task: ")
        CreateTask(Task_List, task_text, False)

    if "done" in command and len(command) == 4 or "d" in command and len(command) == 1:
        task = input("Done Task : ")
        MarkTask(Task_List, int(task), True)

        MarkTaskServer(task, 1)

    if "delete" in command and len(command) == 6 or "de" in command and len(command) == 2:
        task = input("Delete Task : ")
        DeleteTask(Task_List, int(task))

        DeleteTaskServer(task)
    
    if "not done" in command and len(command) == 8 or "n" in command and len(command) == 1:
        task = input("Not Done Task : ")
        MarkTask(Task_List, int(task), False)

        MarkTaskServer(task, 0)
    
    