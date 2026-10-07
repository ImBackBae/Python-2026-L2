from domains import Student, Course, Mark
def get_number(prompt, cast=int, low=None, high=None):
    while True:
        try:
            value = cast(input(prompt))
        except ValueError:
            print("You entered a wrong value, please enter again!")
            continue

        if (low is not None and value < low) or (high is not None and value > high):
            print(f"Please enter a value between {low} and {high}!")
            continue

        return value
        
def input_students(students):
    num = get_number("Enter number of students: ")
    for i in range(num):
        id = input("Enter student id: ")
        name = input("Enter student name: ")
        dob = input("Enter student dob: ")
        students.append(Student(id, name, dob))
    write_students(students)
    return students

def input_courses(courses):
    num = get_number("Enter number of courses: ")
    for i in range(num):
        id = input("Enter course id: ")
        name = input("Enter course name: ")
        credits = get_number("Enter number of credits: ")
        courses.append(Course(id, name, credits))
    write_courses(courses)
    return courses

def input_marks(students, courses, marks):
    if not students or not courses:
        print("Please enter students and courses first!")
        return
    for i in range(len(courses)):
        print(f"{i + 1}) {courses[i].name}")
    c = get_number(f"Choose a course from 1 to {len(courses)}: ",int, 1, len(courses))
    print("================================")
    for i in range(len(students)):
        print(f"{i + 1}) {students[i].name}")
    s = get_number(f"Choose a student from 1 to {len(students)}: ",int, 1, len(students))
    score = get_number("Enter score of this student in the course: ", float, 0, 20.00)
    for mark in marks:
        if mark.student is students[s - 1] and mark.course is courses[c - 1]:
            marks.remove(mark)
            break
    marks.append(Mark(students[s-1], courses[c-1], score))
    write_marks(marks)
    return marks

def write_students(students):
    with open("students.txt", "w") as f:
        for student in students:
            f.write(f"{student.id}|{student.name}|{student.dob}\n")

def write_courses(courses):
    with open("courses.txt", "w") as f:
        for course in courses:
            f.write(f"{course.id}|{course.name}|{course.credits}\n")

def write_marks(marks):
    with open("marks.txt", "w") as f:
        for mark in marks:
            f.write(f"{mark.student.id}|{mark.course.id}|{mark.score}\n")
