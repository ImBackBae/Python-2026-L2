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
        
def input_students():
    num = get_number("Enter number of students: ")
    students = []
    for i in range(num):
        id = input("Enter student id: ")
        name = input("Enter student name: ")
        dob = input("Enter student dob: ")
        students.append(Student(id, name, dob))
    return students

def input_courses():
    num = get_number("Enter number of courses: ")
    courses = []
    for i in range(num):
        id = input("Enter course id: ")
        name = input("Enter course name: ")
        credits = get_number("Enter number of credits: ")
        courses.append(Course(id, name, credits))
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
    return marks
