import colorful as cf
import sqlite3

from TaskHandler import *
from UserInput import *

Task_List = [] 

def main():
    
    ShowTasks(Task_List)
    
    UserInput(Task_List)
  
    UpdateServerData(Task_List)
    
    main()

if __name__ == "__main__":  
    LoadDatabase(Task_List)

    main()
    
