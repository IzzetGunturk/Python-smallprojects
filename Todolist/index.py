tasks = []
devide = "\n---------------------------------------------------------------------\n"

def add_task(task):
    tasks.append(task)
    print("Task added to list")

def remove_task(task):
    tasks.remove(task)
    print("Task removed from list")

def show_tasks():
    print("Tasks:")
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task}")

def main():
    while True:
        print("Options:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Show Tasks")
        print("4. Quit")

        choice = input("Enter your choice:")

        if choice == "1":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "2":
            task = input("Enter the task to remove: ")
            remove_task(task)
        elif choice == "3":
            show_tasks()
            print(devide)
        elif choice == "4":
            print("Bye")
            break
        else:
            print("Error, choose another option")

if __name__ == "__main__":
    main()
