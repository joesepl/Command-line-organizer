Command-Line Task Organizer
This project solidifies your understanding of basic input/output, data structures, and saving data locally. It's a classic for a reason.

Goal: Create a command-line application to manage a to-do list. The user should be able to add tasks, view all tasks, and mark tasks as complete. The list should be saved to a file so it persists between sessions.
Requirements:
When the program starts, it should load any existing tasks from a file.
The user should be presented with a menu of options: 1. Add a task, 2. View all tasks, 3. Mark a task as complete, 4. Quit.
Adding a task prompts the user for a description and adds it to the list.
Viewing tasks prints a numbered list of all current tasks, showing their status (e.g., "[X]" for complete, "[ ]" for incomplete).
Marking a task as complete asks the user for the number of the task to mark.
When the user quits, the current list of tasks is saved back to the file.
Broad Steps:
Start by outlining the main loop of the program that will display the menu and wait for user input.
Implement the logic for adding a task. This will involve getting user input and appending it to a list in memory. A list of dictionaries might be useful here, e.g., {'description': 'Do laundry', 'status': 'incomplete'}.
Implement the viewing logic. Loop through your list of tasks and print them in a formatted way.
Implement the logic for marking a task complete. You'll need to get the task number, validate that it's a valid number, and then update the status of the corresponding task in your list.
Figure out how to save your task list to a file. The json library is excellent for this. Create a function save_tasks() that writes your list to tasks.json.
Create a load_tasks() function that checks if tasks.json exists when the program starts and loads its contents back into your list variable.
Recommended Libraries/Functions:
Built-in: input(), print(), open(), basic list/dictionary manipulation.
Standard Library: json (for json.dump() to save and json.load() to read your data file).
