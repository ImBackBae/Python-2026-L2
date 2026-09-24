
def student_number():
    n = int(input("Enter number of students: "))
    return n

def student_info():
    n = student_number()
    students = []
    for i in range(n):
        print("==================================")
        id = input("Enter student id: ")
        name = input("Enter student name: ")
        dob = input("Enter student date of birth: ")
        students.append([id, name, dob])
    print("==================================")
    return tuple(students)

def course_number():
    n = int(input("Enter course number: "))
    return n

def course_info():
    n = course_number()
    courses = []
    for i in range(n):
        print("==================================")
        id = input("Enter course id: ")
        name = input("Enter course name: ")
        courses.append([id, name])
    print("==================================")
    return tuple(courses)

def input_marks(courses, students):
    courses_num = len(courses)
    students_num = len(students)
    marks = dict()
    while True:
        for i in range(courses_num):
            print("==================================")
            print(f"Course {i+1}) {courses[i][1]}")
        choosing = int(input(f"Choose a course (1-{courses_num}): "))
        if choosing in range(1, courses_num+1):
            while True:
                for j in range(students_num):
                    print("==================================")
                    print(f"Student {j+1}) {students[j][1]}")
                choosing_s = int(input(f"Choose a student (1-{students_num}): "))
                if choosing_s in range(1, students_num+1):
                    mark = input("Enter mark for this student: ")
                    marks.update({tuple([courses[i][0], students[j][0]]) : mark})
                    break
                else:
                    print("You entered a wrong value please enter again!")
                break
            break
        else:
            print("You entered a wrong value please enter again!")
    return marks



def main():
    students = student_info()
    print(students)
    courses = course_info()
    print(courses)
    print(input_marks(courses, students))

main()