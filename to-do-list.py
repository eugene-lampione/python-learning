# create a to-do list management system app
import os

os.system("clear")

'''
Our list will look like this:
tasks = [
    {"task":"walk the dog","completed":False},
    {"task":"take out the trash","completed":False},
    {"task":"take a nap","completed":False},
]

print(tasks[1]) ---> {"task":"Walk the dog","completed":False}
print(tasks[1]["task"]) ---> Walk the dog
print(tasks[1]["completed"]) ---> False
'''

# Add a task to the list
def addTask(tasks, task):
    # append the new task to our task list
    tasks.append({"task":task,"completed":False})
    print(f"Task '{task}' has been added.")
    return tasks

# view the tasks
def viewTasks(tasks):
    if not tasks:
        print("No tasks in the list...")
    else:
        print("\nTo-Do List:")
        '''
        enumerate(thing you want to loop through,number to start at)
        '''
        for idx, taskInfo in enumerate(tasks, 1):
            status = "Done" if taskInfo["completed"] else "Not Done"
            print(f'{idx}. {taskInfo["task"]} - {status}')
    print()

# Remove a task
def removeTask(tasks, taskIndex):
    if 0 <= taskIndex < len(tasks):
        # remove task
        removedTask = tasks.pop(taskIndex)
        print(f'Removed Task: {removedTask["task"]}')
    else:
        print("Invalid Task Number.")
    return tasks

# mark a task as complete
def completeTask(tasks, taskIndex):
    if 0 <= taskIndex < len(tasks):
        # mark task completed
        tasks[taskIndex]["completed"] = True
        print(f'Task: "{tasks[taskIndex]["task"]}" marked as completed.')
    else:
        print("Invalid Task Number.")
    return tasks

# main to do function
def toDoList():
    # create a python list to keep track of to do list
    tasks = []

    while True:
        os.system("clear")

        print("\n---vTo-Do List Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Mark task as completed")
        print("5. Quit")

        choice = int(input("Choose an option: "))

        # Add task
        if choice == 1:
            task = input("Enter the task: ")
            tasks = addTask(tasks, task)
            # tell the user to hit enter
            input("\nPress Enter to continue....") # pause before clearing the screen
        
        # view tasks
        elif choice == 2:
            viewTasks(tasks)
            input("\nPress Enter to continue....") # pause before clearing the screen

        # remove tasks
        elif choice == 3:
            # check to make sure there are tasks
            if tasks:
                viewTasks(tasks) # show the list before prompting to remove one
                taskIndex = int(input("Enter the Task number to remove: ")) - 1
                # call the remove task function and passing task lsit and indext to remove
                tasks = removeTask(tasks, taskIndex)

            else:
                print("There are no tasks to remove...")

            input("\nPress Enter to continue...") # pause before clearing the screen

        # mark task as completed
        elif choice == 4:
            # check to make sure there are tasks
            if tasks:
                viewTasks(tasks) # show the list before prompting to remove one
                taskIndex = int(input("Enter the Task number to mark complete: ")) - 1
                # call the complete task function and passing task list and indext to remove
                tasks = completeTask(tasks, taskIndex)

            else:
                print("There are no tasks to mark complete...")

            input("\nPress Enter to continue...") # pause before clearing the screen

        elif choice == 5:
            print("Exiting To-Do List. Goodbye!")
            break

        else:
            print("Invalid option. Please Try Again")
            input("\nPress Enter to Continue...") # pause before clearing the screen


# run the app
toDoList()