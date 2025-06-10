import json

def main():
    print("Welcome to Jojo's CLI task manager")
    currentOption = menu()
    while currentOption != 6:
        menu_navigation(currentOption)
        currentOption = menu()

    
def menu():
    print("_______________Main Menu___________")
    print("Enter any number to select an option")
    print("1.) Add Task")
    print("2.) View Tasks")
    print("3.) Mark Task Complete")
    print("4.) Save Tasks")
    print("5.) Load Tasks")
    print("6.) quit")
    userInput = int(input("\nEnter Option: "))
    if 1<= userInput <=6:
        print("You entered: ", userInput)
    else:
        print("Please enter a valid number")
        menu()
    return userInput

def menu_navigation(userInput):
    if userInput == 1:
        add_task()
    else:
        return

def add_task():
    print("adding task")
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