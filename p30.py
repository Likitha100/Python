def add_student(name, roll_no, marks, grade):
    return (name, roll_no, marks, grade)

students = []

students.append(add_student("Alice", 101, (85, 90, 88), "A"))
students.append(add_student("Bob", 102, (78, 82, 80), "B"))
students.append(add_student("Charlie", 103, (92, 95, 94), "A+"))

def display_students(student_list):
    print("\nStudent Data:")
    for student in student_list:
        name, roll_no, marks, grade = student
        print(f"Name: {name}, Roll No: {roll_no}, Marks: {marks}, Grade: {grade}")

def display_average_marks(student_list):
    print("\nAverage Marks of Students:")
    for student in student_list:
        name, _, marks, _ = student
        avg = sum(marks) / len(marks)
        print(f"{name}'s average marks: {avg:.2f}")

def search_student_by_roll(student_list, roll_no):
    print(f"\nSearching for student with Roll No: {roll_no}")
    for student in student_list:
        if student[1] == roll_no:
            print("Student found:")
            print(f"Name: {student[0]}, Marks: {student[2]}, Grade: {student[3]}")
            return
    print("Student not found.")
--
display_students(students)
display_average_marks(students)
search_student_by_roll(students, 102)
