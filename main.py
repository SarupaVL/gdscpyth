#remember that this is a menu driven program

""" import typer
app=typer.Typer()

@app.command()
def hello():
    print("helloooo")

@app.command()
def goodbye():
    print("Goodbye")

if __name__=="__rept__":
    app() """

""" def main():

    #initializing an empty kanban boards' list
    boards=[]
    todo={"Task name":[],"Description":[],"Assignees":[],"Reporters":[],"Priority":[]}
    doing={"Task name":[],"Description":[],"Assignees":[],"Reporters":[],"Priority":[]}
    done={"Task name":[],"Description":[],"Assignees":[],"Reporters":[],"Priority":[]}

    choice=0
    while choice!=5:
        print("1. Create a new kanban board")
        print("2. Edit existing kanban board")
        print("3. Delete kanban board")
        print("4. Display a kanban board")
        print("5. Exit")
        choice=int(input("Enter your choice:"))

        if choice==1:
            print("Creating a new kanban board...")
            kb=input("Enter name of the new board")
            boards.append(kb)

            print("Lets add your tasks in their respective boxes!")
            dywc=""
            while dywc!="no":
                tname=input("Enter task name: ")
                tstat=input("Todo/Doing/Done: ")
                tdesc=input("Enter task description: ")
                tassi=input("Enter assignees: ")
                trepo=input("Enter reporters: ")
                tprio=input("Enter priority (high,medium,low): ")
                if tstat=="Todo":
                    todo["Task name"]+=[tname]
                    todo["Description"]+=[tdesc]
                    todo["Assignees"]+=[tassi]
                    todo["Reporters"]+=[trepo]
                    todo["Priority"]+=[tprio]
                elif tstat=="Doing":
                    doing["Task name"]+=[tname]
                    doing["Description"]+=[tdesc]
                    doing["Assignees"]+=[tassi]
                    doing["Reporters"]+=[trepo]
                    doing["Priority"]+=[tprio]
                elif tstat=="Done":
                    done["Task name"]+=[tname]
                    done["Description"]+=[tdesc]
                    done["Assignees"]+=[tassi]
                    done["Reporters"]+=[trepo]
                    done["Priority"]+=[tprio]
                dywc=input("Do you wanna continue adding tasks? (yes/no): ")

        if choice==4:
            print(todo)
            print(doing)
            print(done)

if __name__=="__main__":
    main() """


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

            print("Lets add your tasks in their respective boxes!")
            add_tasks(new_board)

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
