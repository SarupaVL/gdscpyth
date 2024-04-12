
#code to make things look fancy
import os
def print_msg_box(msg, indent=1, width=None, title=None):
    """Print message-box with optional title."""
    lines = msg.split('\n')
    space = " " * indent
    if not width:
        width = max(map(len, lines))
    box = f'╔{"═" * (width + indent * 2)}╗\n'
    if title:
        box += f'║{space}{title:<{width}}{space}║\n'
        box += f'║{space}{"-" * len(title):<{width}}{space}║\n'
    box += ''.join([f'║{space}{line:<{width}}{space}║\n' for line in lines])
    box += f'╚{"═" * (width + indent * 2)}╝'
    print(box)

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

        msg = "1. Create a new kanban board\n" \
            "2. Edit existing kanban board\n" \
                "3. Delete a kanban board\n" \
                    "4. Display a kanban board\n" \
                        "5. Exit"

        print_msg_box(msg=msg, indent=2, title='What do you want to do?')

        '''
        print("1. Create a new kanban board")
        print("2. Edit existing kanban board")
        print("3. Delete kanban board")
        print("4. Display a kanban board")
        print("5. Exit")
        '''
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Creating a new kanban board...")
            kb_name = input("Enter name of the new board: ")
            new_board = KanbanBoard(kb_name)
            boards.append(new_board)

            print("Lets add your tasks in their respective boxes!!!")
            add_tasks(new_board)

        if choice == 2:
            kb_namee = input("Enter name of the kanban board to be edited: ")
            choicea = 0
            while choicea!=3:
                print("1. Adding a task")
                print("2. Deleting a task")
                print("3. Exit")
                choicea=int(input("Enter your choice: "))

                for board in boards:
                    if board.name == kb_namee:
                        if choicea == 1:
                            add_tasks(board)
                        elif choicea == 2:
                            delete_task_name = input("Enter the name of the task to delete: ")
                            delete_task_status = input("Enter the status of the task (Todo/Doing/Done): ")
                            if board.delete_task(delete_task_name, delete_task_status):
                                print("Task deleted successfully!")
                            else:
                                print("Task not found!")
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
            for board in boards:
                if board.name == kb_nameee:
                    boards.remove(board)
                    print("Kanban board deleted successfully!")
                    break
                else:
                    print("Kanban board not found!")

        if choice == 4:
            #print priority wise
            kb_nam=input("Enter the name of kanban board to be printed: ")
            for board in boards:
                if board.name == kb_nam:
                    term_size = os.get_terminal_size()
                    print('=' * term_size.columns)
                    print(board.name,"\n")
                    print('=' * term_size.columns)

                    """ sorted_todo = sorted(board.todo, key=lambda x: x.priority)
                    sorted_doing = sorted(board.doing, key=lambda x: x.priority)
                    sorted_done = sorted(board.done, key=lambda x: x.priority) """

                    print("Todo:\n")
                    for task in board.todo:
                        print_task(task)
                    print('=' * term_size.columns)

                    print("Doing:\n")
                    for task in board.doing:
                        print_task(task)
                    print('=' * term_size.columns)

                    print("Done:\n")
                    for task in board.done:
                        print_task(task)
                    print('=' * term_size.columns)
                else:
                    print("Kanban board not found!")

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
