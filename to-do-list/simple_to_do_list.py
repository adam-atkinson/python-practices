tasks = []

while True:
    print("\n===To-Do List Menu===")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")
    if choice == "1":
        if len(tasks) == 0:
            print("Your to-do list is empty.")
        else:
            print("\nYour Tasks:")
            for task in tasks:
                print("-", task)

    elif choice == "2":
        new_task = input("Enter a new task: ")
        tasks.append(new_task)
        print("Task added.")

    elif choice == "3":
        remove_task = input("Enter the task you want to remove: ")
        if remove_task in tasks:
            tasks.remove(remove_task)
            print("Task removed.")
        else:
            print("Task not found in the list.")

    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please choose between 1 and 4.")

