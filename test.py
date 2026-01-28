class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades  # list of numbers

    def calculate_average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

    def check_pass_fail(self):
        avg = self.calculate_average()
        return "Pass" if avg >= 50 else "Fail"

    def print_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {self.grades}")
        print(f"Average: {self.calculate_average():.2f}")
        print(f"Result: {self.check_pass_fail()}")
        print("-" * 30)


# -------------------------------
# Dynamic Student Management
# -------------------------------

students = []

while True:
    print("\n--- Student Management Menu ---")
    print("1. Add new student")
    print("2. Show all students")
    print("3. Save records to file")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        grades = input("Enter grades separated by commas: ")
        grades_list = [int(g.strip()) for g in grades.split(",")]
        students.append(Student(name, age, grades_list))
        print("Student added successfully!")

    elif choice == "2":
        if not students:
            print("No student records yet.")
        else:
            for s in students:
                s.print_details()

    elif choice == "3":
        with open("students.txt", "w") as f:
            for s in students:
                f.write(f"{s.name},{s.age},{s.grades},{s.calculate_average():.2f},{s.check_pass_fail()}\n")
        print("Records saved to students.txt")

    elif choice == "4":
        print("Exiting program... Goodbye!")
        break

    else:
        print("Invalid choice, try again.")
