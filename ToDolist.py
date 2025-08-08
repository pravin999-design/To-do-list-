
tasks = []

def shows():
    print("\n -----To Do list Menu ------")
    print("1 . Add Task")
    print("2. View Task")
    print("3. Mark To Be Done")
    print("4. Delete The Task")
    print("5. Exit")

def Add_Task():
    task_name = input("Enter The Task Description")
    tasks.append({"Task": task_name} , {"Done" : False})
    print("The Task Added Successfully")

def View_task():
    if not tasks:
        print("No Task Available")
    else:
        for i , task in enumerate(tasks):
            status = "Done"  if task ["Done"] else "Not done"
            print(f"{i+1}, {task["task"]}- {status}")

def Mark_Done():
    View_task()
    task_no = input("Enter The Task number to mark as done")
    if 0<= task_no <len(tasks):
        tasks[task_no] ["Done"] = True
        print("Task Marked as Done")
    else:
        print("Invalid Task Number")

def Delete_Task():
    View_task()
    task_no = input('Enter The Task number to Delete the Task')
    if 0<= task_no <len(tasks):
        removed = tasks.pop(task_no)
        print(f"Deleted Task : {removed['task']}")
    else:
        print("Invalid Task Number ")


while True:
    shows()
    choice = input("Enter your Choice (1-5)")

    if choice==1 :
        Add_Task()
    elif choice==2 :
        View_task()
    elif choice==3 :
        Mark_Done()
    elif choice==4:
        Delete_Task()
    elif choice == 5:
        print("THanks For Using To Do App ")
    else:
        print("Invalid input Number . Please try again")