import os
import colorful as cf

def ShowTasks(Task_List):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("----------Tasks----------")

    for index, task in enumerate(Task_List): 
        if(task.status == True):
           
            print(cf.green(str(index) + " : " + "[x] "+ task.text))
        else:
            print(cf.red(str(index) + " : " + "[] " + task.text))


def CreateTask(Task_List, text, status):
     Task_List.append(Task(text, status))


def MarkTask(Task_List, id, status):
    Task_List[id].status = status

def DeleteTask(Task_List, id):
    
    Task_List.pop(id)


class Task:
    def __init__(self, text, status):
        self.text = text
        self.status = status
