grades={}

while True:
    print(" enter 1 to add a student")
    print(" enter 2 to update student grades")
    print(" enter 3 to print all student grades")
    print(" enter 4 to exit")
    print("Welcome to the Student Grades Management System")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter student grade: ")
        grades[name] = grade
        print("Student added.")
    elif choice == "2":
        name = input("Enter student name to update: ")
        if name in grades:
            grade = input("Enter new grade for student: ")
            grades[name] = grade
            print("Student grade updated.")
        else:
            print("Student not found.")
    elif choice == "3":
        print("All Student Grades:")
        for name, grade in grades.items():
            print(f"{name}: {grade}")
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")