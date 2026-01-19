List = []

while True:
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter the task to add: ")
        List.append(task)
        print(f'Task "{task}" has been added to your to-do list.') 

    if choice == '2':
        if not List:
            print("Your to-do list is empty.")
        else:
            print("Your To-Do List:")
            for idx, task in enumerate(List, start=1):
                print(f"{idx}. {task}")  


    if choice == '3':
        task = input("Enter the task to remove: ")
        if task in List:
            List.remove(task)
            print(f'Task "{task}" has been removed from your to-do list.')
        else:
            print(f'Task "{task}" not found in your to-do list.')

    if choice == '4':
        print("Exiting To-Do List App. Goodbye!")
        break
            