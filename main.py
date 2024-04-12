class Task:
    def __init__(self, name, description, assignees, reporters, priority):
        self.name = name
        self.description = description
        self.assignees = assignees
        self.reporters = reporters
        self.priority = priority

class KanbanBoard:
    def __init__(self, name):
        self.name = name
        self.todo = []
        self.doing = []
        self.done = []

    def add_task(self, task, status):
        if status == "Todo":
            self.todo.append(task)
        elif status == "Doing":
            self.doing.append(task)
        elif status == "Done":
            self.done.append(task)

    def delete_task(self, task_name, status):
        if status == "Todo":
            for task in self.todo:
                if task.name == task_name:
                    self.todo.remove(task)
                    return True
        elif status == "Doing":
            for task in self.doing:
                if task.name == task_name:
                    self.doing.remove(task)
                    return True
        elif status == "Done":
            for task in self.done:
                if task.name == task_name:
                    self.done.remove(task)
                    return True
        return False
            

def main():
    boards = []

    choice = 0
    while choice != 5:
        print("1. Create a new kanban board")
        print("2. Edit existing kanban board")
        print("3. Delete kanban board")
        print("4. Display a kanban board")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Creating a new kanban board...")
            kb_name = input("Enter name of the new board: ")
            new_board = KanbanBoard(kb_name)
            boards.append(new_board)

            print("Lets add your tasks in their respective boxes!!!")
            add_tasks(new_board)

        if choice == 2:
            choicea = 0
            while choicea!=3:
                print("1. Adding a task")
                print("2. Deleting a task")
                print("3. Exit")
                choicea=int(input("Enter your choice: "))

                kb_namee = input("Enter name of the kanban board to be edited: ")

                for board in boards:
                    if board.name == kb_namee:
                        if choicea == 1:
                            board.add_task()
                        elif choicea == 2:
                            board.delete_task()
                        elif choicea == 3:
                            break
                        else:
                            print("Invalid choice!")
                        break
                else:
                    print("Kanban board not found!")

        if choice == 3:
            print("Deleting a kanban board...")
            kb_nameee=input("Enter the name of kanban board to be deleted: ")
            boards.remove("kb_nameee")

        if choice == 4:
            for board in boards:
                print(board.name)
                print("Todo:")
                for task in board.todo:
                    print_task(task)
                print("Doing:")
                for task in board.doing:
                    print_task(task)
                print("Done:")
                for task in board.done:
                    print_task(task)

def add_tasks(board):
    dywc = ""
    while dywc != "no":
        tname = input("Enter task name: ")
        tstat = input("Todo/Doing/Done: ")
        tdesc = input("Enter task description: ")
        tassi = input("Enter assignees: ")
        trepo = input("Enter reporters: ")
        tprio = input("Enter priority (high, medium, low): ")

        new_task = Task(tname, tdesc, tassi, trepo, tprio)
        board.add_task(new_task, tstat)

        dywc = input("Do you wanna continue adding tasks? (yes/no): ")

def print_task(task):
    print("Name:", task.name)
    print("Description:", task.description)
    print("Assignees:", task.assignees)
    print("Reporters:", task.reporters)
    print("Priority:", task.priority)
    print()

if __name__ == "__main__":
    main()
