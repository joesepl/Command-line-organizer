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
    print("2.) Delete Task")
    print("3.) View Tasks")
    print("4.) Mark Task Complete")
    print("5.) Save Tasks")
    print("6.) Load Tasks")
    print("7.) quit")
    try: userInput =int(input("\nEnter Option: "))
    except: 
        print("Please enter a valid number")
        return
    
    if not(1<= userInput <=7):
        print("Please enter a valid number")
    return userInput

def menu_navigation(userInput, tasks):
    if userInput == 1:
        add_task(tasks)
    elif userInput == 2:
        delete_task(tasks)
    elif userInput == 3:
        view_tasks(tasks)
    elif userInput == 4:
        mark_task_complete(tasks)
        return

def add_task(tasks):
    taskName = input("Enter the task (q to return): ")
    if taskName == "q":
        return
    tasks [taskName] = "incomplete"
    print("The task ", taskName, " has been added.")
    add_task(tasks)

def view_tasks(tasks):
    #Iterate through tasks and print them. If a task is complete represent it with an x. 
    print("\nFull Task List")
    ctr = 1
    for task in tasks:
        print(ctr, ".) ", task, end='')
        if tasks[task] == "incomplete":
            print(" [ ] ")
        else:
            print(" [X] ")
        ctr += 1

def mark_task_complete(tasks):
    view_tasks(tasks)
    numOfTask = int(input("Enter the number of the task to mark completed: "))
    cntr = 1
    for task in tasks:
        if numOfTask == cntr:
            print ("Marking ", task, "as complete.")
            tasks[task] = "complete"
        cntr +=1

def delete_task(tasks):
    view_tasks(tasks)
    numOfTask = int(input("Enter the number of the task to delete: "))
    taskChosen = ""
    cntr = 1
    for task in tasks:
        if numOfTask == cntr:
            print ("Deleting ", task, "...")
            taskChosen = task
        cntr +=1
    del tasks[taskChosen]

#def save_tasks():
#def load_tasks():





if __name__ == "__main__":
    main()



""" 
_______GIT NOTES_______
git add .                                           #Stage the files you want to commit
git commit -m "Implemented the add task feature"    #commit the staged files with a descriptive message
git push                                            #To upload commit

# --- Checking on Your Work ---
git status                # Shows what's changed, what's staged, and what's untracked.
git diff                  # Shows the exact line-by-line changes in your modified (but unstaged) files.
git diff --staged         # Shows the line-by-line changes for files you have already staged (added).

# --- Viewing Your Project's History ---
git log                   # Displays a detailed, chronological list of all commits.
git log --oneline         # Displays a simplified, one-line view of the commit history.
git log --graph --oneline --all # Displays a visual graph of all branches and their commit histories.

# --- Undoing Mistakes ---
git restore <file>        # Discards all unstaged changes in a file, reverting it to the last commit. (Use with caution!)
git restore --staged <file> # Removes a file from the staging area ("un-adds" it) but keeps the changes.
git commit --amend        # Allows you to modify your most recent commit (e.g., to fix the message or add a forgotten file).

# --- Working with Branches ---
git branch <branch-name>  # Creates a new branch without switching to it.
git switch <branch-name>  # Switches your current workspace to the specified branch.
git branch                # Lists all the branches in your local repository and shows which one you are on.
git merge <branch-name>   # Combines the history from the specified branch into your currently active branch.
git branch -d <branch-name> # Deletes a local branch (typically after it has been merged).

# --- Syncing with a Remote Repository (like GitHub) ---
git clone <url>           # Downloads a repository from a URL to your local machine.
git add <file>            # Stages a file, preparing it for the next commit. (Use '.' to add all files).
git commit -m "Message"   # Saves your staged changes as a snapshot in the project's history.
git push                  # Uploads your committed changes to the remote repository (e.g., GitHub).
git pull                  # Fetches changes from the remote repository and merges them into your current branch.



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