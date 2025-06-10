import json

def main():
    print("Welcome to Jojo's CLI task manager")
    tasks = {}
    currentOption = menu()
    while currentOption != 6:
        menu_navigation(currentOption, tasks)
        currentOption = menu()

    
def menu():
    print("\n_______________Main Menu___________")
    print("Enter any number to select an option")
    print("1.) Add Task")
    print("2.) View Tasks")
    print("3.) Mark Task Complete")
    print("4.) Save Tasks")
    print("5.) Load Tasks")
    print("6.) quit")
    try: userInput =int(input("\nEnter Option: "))
    except: 
        print("Please enter a valid number")
        return
    
    if not(1<= userInput <=6):
        print("Please enter a valid number")
    return userInput

def menu_navigation(userInput, tasks):
    if userInput == 1:
        add_task(tasks)
    else:
        return

def add_task(tasks):
    taskName = input("Enter the task you would like to add: ")
    tasks [taskName] = "incomplete"
    print("The task ", taskName, " has been added.")

#def view_tasks():
#def mark_task_complete():
#def save_tasks():
#def load_tasks():





if __name__ == "__main__":
    main()



""" 
_______GIT NOTES_______
git add .                                           //Stage the files you want to commit
git commit -m "Implemented the add task feature"    //commit the staged files with a descriptive message
git push                                            //To upload commit

_______JSON NOTES_______
import json

tasks = [
    {'description': 'Do laundry', 'status': 'incomplete'},
    {'description': 'Buy groceries', 'status': 'incomplete'}
]

# The 'w' means we are writing to the file.
with open('tasks.json', 'w') as file:
    json.dump(tasks, file)

import json

try:
    # The 'r' means we are reading the file.
    with open('tasks.json', 'r') as file:
        tasks = json.load(file)
except FileNotFoundError:
    # If the file doesn't exist, start with an empty list.
    tasks = []

print(tasks)

"""