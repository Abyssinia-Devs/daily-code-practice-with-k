

tasks = []

def load_task():
    with open("tasks.txt", "r") as file :
        for line in file:
            tasks.append(line.strip())


def save_tasks():
    with open("tasks.txt", "w")as file :
        for task in tasks:
            file.write( task + "\n")


def view_tasks(tasks=None):
        if len(tasks) ==0:
            print("\nNo tasks yet!")
        else:
            print("\nYour Tasks:")
            for i,tasks in enumerate(tasks,1):
                print(f"{i}. {tasks}")
                print()


def add_task():
    name = input("Enter the name of the new task: ")
    tasks.append(name + "Not completed")
    save_tasks()
    print("task added!\n")


def edit_task():
    view_tasks()
    if len(tasks) ==0:
        return
    num = int(input("Which task number do you want to edit? "))
    new_name = input("Enter new task name: ")
    tasks[num - 1] = new_name  + "(Not completed )"
    save_tasks()
    print("Task updated!\n")


def complete_task():
    view_tasks()
    if len(tasks) == 0:
        return
    num = int(input("Which   task number do you finish? "))
    task = tasks[num -1]
    tasks[num - 1] = task.replace("(Not completed)", "(Completed)")
    save_tasks()
    print("Tasks marked as completed!\n")


def delete_task():
    view_tasks()
    if len(tasks) == 0:
        return
    else :
        num = int(input("Which task do you want to delete? "))
        tasks.pop(num -1)
        save_tasks()
        print("Task deleted!\n")

def main():
    load_task()

    while True:
        print("----TO-DO LIST MENU ----")
        print("1, Add Task")
        print("2, View Task")
        print("3, Edit Task")
        print("4, Mark Task as Complete")
        print("5, Delete Task")
        print("6, Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            edit_task()
        elif choice == "4":
            complete_task()
        elif choice == "5":
            delete_task()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")

main()
