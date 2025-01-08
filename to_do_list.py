def to_do_list():
    print ("Welcome to the To-Do List app")
    
    tasks = []
    
    while True:
        print("\nSelect a choice")
        print ("1. Add Task")
        print ("2. View Tasks")
        print ("3. Remove Task")
        print ("4. Exit")

        choice = (input("Enter you choice: "))

        if choice == "4":
            print ("Goodbye! Thanks for using our app")
            break

        if choice not in ["1", "2", "3", "4"]:
            print ("Invalid choice. Please try again")
            continue

    
        if choice == "1":
            task = input("Enter the task you want to add: ")
            tasks.append(task)
            print (f"Task '{task}' added to the list!")
        elif choice == "2":
            if not tasks:
                print("Your task list is empty!")
            else:
                print("Here are your tasks:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")
        elif choice == "3":
            if not tasks:
                print ("Your task list is empty, nothing to remove!")
            else:
                print ("Here are your tasks:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task}")
                try:
                    task_number = int(input("Enter the task number to remove: "))
                    if 1 <= task_number <= len(tasks):
                        removed_task = tasks.pop(task_number - 1)
                        print (f"Task '{removed_task}' removed!")
                    else:
                        print("Invalid task number!")
                except ValueError:
                    print("Please enter a valid number!")


        to_do_list()