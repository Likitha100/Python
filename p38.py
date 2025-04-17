students = [
    ("Alice", 101, (85, 90, 88), "A"),
    ("Bob", 102, (70, 65, 72), "B"),
    ("Charlie", 103, (95, 91, 94), "A+")
]

def display_students():
    print("\nAll Students:")
    for student in students:
        print(student)

def add_student(name, roll, marks, grade):
    students.append((name, roll, marks, grade))
    print(f"\nStudent {name} added.")

def search_student(roll):
    for student in students:
        if student[1] == roll:
            print("\nStudent found:", student)
            return
    print("\nStudent not found.")

def calculate_total_marks():
    print("\nTotal Marks:")
    for student in students:
        total = sum(student[2])
        print(f"{student[0]} (Roll {student[1]}): Total Marks = {total}")

def update_grade(roll, new_grade):
    for i, student in enumerate(students):
        if student[1] == roll:
            updated_student = (student[0], student[1], student[2], new_grade)
            students[i] = updated_student
            print(f"\nGrade updated for Roll {roll}.")
            return
    print("\nStudent not found.")

def remove_student(roll):
    for i, student in enumerate(students):
        if student[1] == roll:
            removed = students.pop(i)
            print(f"\nStudent {removed[0]} removed.")
            return
    print("\nStudent not found.")

display_students()
add_student("David", 104, (78, 82, 80), "B+")
search_student(102)
calculate_total_marks()
update_grade(102, "A-")
remove_student(101)
display_students()