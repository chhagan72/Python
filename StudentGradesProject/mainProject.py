#Initialising Dectionary
std_grade={}

#Add the new student in the dectionary
def add_std(name, grade):
    std_grade[name] = grade
    print(f"Added {name} with a {grade}")

def update_std(name, grade):
    if name in std_grade:
        std_grade[name]= grade
        print(f"{name} with marks are updated {grade}")
    else:
        print(f"{name} is not found in the dictionary")
def del_std(name):
    if name in std_grade:
        del std_grade[name]
        print(f"{name} is deleted")
    else:
        print(f"{name} is not found in the dectionary")

def displayAll_std():
    if std_grade:
        for name, grade in std_grade.items():
            print(f"{name}:{grade}")
    else:
        print("No Record found in the dectionary")

def main():
    while True:
        print("\n Student Grade management system")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View Student")
        print("5. Exit Student")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            name = input("Enter the name of the student: ")
            grade = int(input("Enter Grade of the student: "))
            add_std(name, grade)
        elif choice == 2:
            name = input("Enter the name of the student: ")
            grade = int(input("Enter Grade of the student: "))
            update_std(name, grade)
        elif choice == 3:
            name = input("Enter the name of the student: ")
            del_std(name)
        elif choice == 4:
            displayAll_std()
        elif choice == 5:
            print("Closing the program.........")
            break
        else:
            print("Invalid choice")
main()

        
