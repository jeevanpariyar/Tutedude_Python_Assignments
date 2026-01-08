# Dictionary with 4 students and their grades
students = {
    "raj": "A",
    "jeevan": "B",
    "priya": "A",
    "akash": "C"
}

while True:
    print("\nChoose an option:")
    print("1. Add a new student")
    print("2. Update student grade")
    print("3. Display all student grades")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    # Add a new student
    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter student grade: ")
        students[name] = grade
        print("Student added successfully.")

    # Update an existing student's grade
    elif choice == "2":
        name = input("Enter student name to update: ")
        if name in students:
            grade = input("Enter new grade: ")
            students[name] = grade
            print("Grade updated successfully.")
        else:
            print("Student not found.")

    # Display all student grades
    elif choice == "3":
        print("\nStudent Grades:")
        for name, grade in students.items():
            print(name, ":", grade)

    # Exit program
    elif choice == "4":
        print("Exiting program. Thank you!")
        break

    else:
        print("Invalid choice. Please enter 1 to 4.")
