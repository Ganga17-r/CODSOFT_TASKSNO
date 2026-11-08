'''Create an empty list named tasks.
Ask the user to enter a task using input().
Add that task to the list using .append().
Print the complete task list.'''
'''tasks=[]
while True:
    new_task=input("Enter a task or(type done to finish):")
    if new_task.lower() =="done":
        break
    tasks.append(new_task)
print("\nYour To-Do List:")
for index, task in enumerate(tasks, start=1):
   print(f"{index}. {task}")
'''
'''Create empty task list
 Repeat:
    Ask user for a task
    Add task to list
    Ask whether they want another task
Stop when user says no
Display all tasks'''
tasks = []

while True:
    choice = input("Enter 1 to add, 2 to view, 3 to exit, 4 to remove, 5 to mark as completed: ")

    if choice == "1":
        task = input("Enter task: ").strip()
        if task == "":
            print("Task cannot be empty!")
        else:
            tasks.append({"title": task, "done": False})
            print("Task added successfully!")

    elif choice == "2":
        if not tasks:
            print("No tasks in the list.")
        else:
            print("\nYour tasks:")
            for index, task in enumerate(tasks, start=1):
                if task["done"]:
                    status = "Completed"
                else:
                    status = "Pending"
                print(f"{index}. {task['title']} - {status}")

    elif choice == "3":
        print("Goodbye!")
        break

    elif choice == "4":
        if not tasks:
            print("No tasks to remove.")
        else:
            print("\nYour tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task['title']}")
            try:
                task_index = int(input("Enter task number to remove: ")) - 1
                if 0 <= task_index < len(tasks):
                    removed_task = tasks.pop(task_index)
                    print(f"Removed task: {removed_task['title']}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "5":
        if not tasks:
            print("No tasks to mark as completed.")
        else:
            print("\nYour tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task['title']}")
            try:
                task_index = int(input("Enter task number to mark as completed: ")) - 1
                if 0 <= task_index < len(tasks):
                    tasks[task_index]["done"] = True
                    print(f"Marked as completed: {tasks[task_index]['title']}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    else:
        print("Invalid choice!")