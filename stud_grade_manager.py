students = {}

def add_student():
    name = input("Enter student name: ").strip()
    if not name:
        print("Error: Name cannot be empty.")
        return
    if name in students:
        print("Student already exists.")
    else:
        students[name] = []
        print("Student added!")

def add_grade():
    name = input("Enter student name: ").strip()
    if not name:
        print("Error: Name cannot be empty.")
        return
    if name not in students:
        print("Student not found.")
        return
    try:
        grade = float(input("Enter grade: "))
        students[name].append(grade)
        print("Grade added!")
    except ValueError:
        print("Error: Invalid grade! Please enter a number.")

def view_students():
    if not students:
        print("No students in the system.")
        return
    print("\n----------- STUDENT LIST -----------")
    for name, grades in students.items():
        if grades:
            avg = sum(grades) / len(grades)
            print(f"{name} -> Grades: {grades} | Avg: {avg:.2f}")
        else:
            print(f"{name} -> Grades: {grades} | Avg: N/A")
    print("------------------------------------")

def top_student():
    if not students:
        print("No students available.")
        return
    best_name = None
    best_avg = -1

    for name, grades in students.items():
        if grades:
            avg = sum(grades) / len(grades)
            if avg > best_avg:
                best_avg = avg
                best_name = name

    if best_name:
        print(f"Top Student: {best_name} with average {best_avg:.2f}")
    else:
        print("No grades entered yet.")

def delete_student():
    name = input("Enter student name to delete: ").strip()
    if not name:
        print("Error: Name cannot be empty.")
        return
    if name in students:
        del students[name]
        print("Student deleted.")
    else:
        print("Student not found.")

def main():
    while True:
        print("\n========== STUDENT GRADE MANAGER ==========")
        print("1. Add Student")
        print("2. Add Grade")
        print("3. View All Students")
        print("4. Show Top Student")
        print("5. Delete Student")
        print("6. Exit")
        print("===========================================")

        choice = input("Choose option: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            add_grade()
        elif choice == "3":
            view_students()
        elif choice == "4":
            top_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1–6.")

if __name__ == "__main__":
    main()
    
