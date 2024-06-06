# TASK 1: TO BUILD A TO-DO-LIST APPLICATION

# BLUEPRINT FOR ALL OBJECTS
class Task :
    def __init__ (self, desc):
        self.desc = desc
        self.completed = False

    def __str__ (self):
        if self.completed==True :
            status = "✓"
        else:
            status="✗"
        return f"[{status}] {self.desc}"

    def mark_completed(self):
        self.completed= True

#List of options
class ToDoLists:
    def __init__(self):
        self.tasks=[]

    def create_task(self, desc):
        task=Task(desc)
        self.tasks.append(task)

    def display_task(self):
        for i, task in enumerate (self.tasks ,1):
            print(f"{i}. {task}")
            
    def update_task(self, tnum, newdesc):
        try:
            self.tasks[tnum-1].desc=newdesc
        except IndexError:
            print("Index out of range")
        print("Updated")

    def mark_task_comp(self, tnum):
        if 0< tnum <=len(self.tasks):
            self.tasks[tnum-1].mark_completed()
        else:
            print("Index out of range")

#USER INTERFACE
def main():
    todolist = ToDoLists()
    while True:
        print("\nEasy To-Do List User Application")
        print("1. CREATE Task")
        print("2. DISPLAY Tasks")
        print("3. UPDATE Task")
        print("4. MARK Task as COMPLETED")
        print("5. EXIT")

        choice = input("Choose an option: ")
        if choice == "1":
            description = input("Enter the task description: ")
            todolist.create_task(description)
        elif choice == "2":
            todolist.display_task()
        elif choice == "3":
            tnum=int(input("Enter the task number to be updated :"))
            newdesc=input("Enter the task's new details:")
            todolist.update_task(tnum, newdesc)
        elif choice == "4":
            tnum=int(input("Enter the task number to be Marked as completed :"))
            todolist.mark_task_comp(tnum)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
            

main()

        











































        
       
        
