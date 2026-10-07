
import math
import numpy as np
import curses
def get_number(prompt, cast=int):
    while True:
        try:
            return cast(input(prompt))
        except ValueError:
            print("Please enter a valid number!")

def student_number():
    n = get_number("Enter number of students: ")
    return n

def student_info():
    n = student_number()
    students = []
    gpa = None
    for i in range(n):
        print("==================================")
        id = input("Enter student id: ")
        name = input("Enter student name: ")
        dob = input("Enter student date of birth: ")
        students.append([id, name, dob, gpa])
    print("==================================")
    return tuple(students)

def course_number():
    n = get_number("Enter course number: ")
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

def input_marks(courses, students, marks):
    if not courses or not students:
        print("Please enter students and courses first!")
    return
    while True:
        print("==================================")
        for i in range(len(courses)):
            print(f"Course {i+1}) {courses[i][1]}")
        c = int(input(f"Choose a course (1-{len(courses)}): "))
        if 1 <= c <= len(courses):
            break
        print("You entered a wrong value please enter again!")

    while True:
        print("==================================")
        for j in range(len(students)):
            print(f"Student {j+1}) {students[j][1]}")
        s = int(input(f"Choose a student (1-{len(students)}): "))
        if 1 <= s <= len(students):
            break
        print("You entered a wrong value please enter again!")

    mark = get_number("Enter mark for this student: ", float)
    course_id = courses[c - 1][0]
    student_id = students[s - 1][0]
    marks[(student_id, course_id)] = math.floor(mark)

def calculate_gpa(marks, students, courses):
    new_students = np.array(students)
    for i in range(len(students)):
        gpa = 0
        for j in range(len(courses)):
            gpa += marks.get((students[i][0], courses[j][0]), 0)
        gpa /= len(courses)
        new_students[i][3] = math.floor(gpa)
    return new_students

def sort_students(s):
    gpa = s[:,-1].astype(float)
    return s[gpa.argsort()[::-1]]

def show_students(students, courses, marks):
    student = 0
    s_options = []
    gpa = calculate_gpa(marks, students, courses)
    for i in range(len(students)):
        s_options.append(f"{int(students[i][0])+1}. {students[i][1]}")
    s_options.append("Back to main menu")
    while True:
        student = curses.wrapper(choosing, s_options)
        if s_options[student] == s_options[-1]:
            break
        else:
            courses_marks = []
            for i in range(len(courses)):
                courses_marks.append(f"{i+1}. {courses[i][1]}: {marks.get((students[student][0], courses[i][0]), 'N/A')}")
            courses_marks.append(f"GPA: {gpa[student][3]}")
            courses_marks.append("Back to students list")
            n = curses.wrapper(choosing, courses_marks)

def show_courses(courses, students, marks):
    course = 0
    c_options = []
    for i in range(len(courses)):
        c_options.append(f"{int(courses[i][0])+1}. {courses[i][1]}")
    c_options.append("Back to main menu")
    while True:
        course = curses.wrapper(choosing, c_options)
        if c_options[course] == c_options[-1]:
            break
        else:
            students_marks = []
            for i in range(len(students)):
                students_marks.append(f"{i+1}. {students[i][1]}: {marks.get((students[i][0], courses[course][0]), 'N/A')}")
            students_marks.append("Back to courses list")
            m = curses.wrapper(choosing, students_marks)

# n = calculate_gpa(marks, students, courses)
# n = sort_students(n)

# print(list(n))

def draw_header(stdscr, title):
    stdscr.addstr(0, 0, title, curses.A_BOLD)

def draw_screen(stdscr, l, selected):
    for i in range(len(l)):
        if i == selected:
            attr = curses.A_REVERSE
        else:
            attr = curses.A_NORMAL
        stdscr.addstr(2 + i, 2, l[i], attr)

def choosing(stdscr, options):
    curses.curs_set(0)
    selected = 0
    while True:
        stdscr.clear()
        draw_header(stdscr, "Welcome to the Students Management Program")
        draw_screen(stdscr, options, selected)
        stdscr.refresh()
        key = stdscr.getch()
        if key == curses.KEY_UP and selected > 0:
            selected -= 1
        elif key == curses.KEY_DOWN and selected < len(options) - 1:
            selected += 1
        elif key in (curses.KEY_ENTER, 10, 13):
            return selected
        
def main():
    students, courses, marks = [], [], {}

    menu_options = ["1)Enter students info", "2)Enter courses info", "3)Enter students marks", "4)Show students", "5)Show courses", "6)Exit"]
    while True:
        choice = curses.wrapper(choosing, menu_options)
        if choice == 0:
            students = student_info()
        elif choice == 1:
            courses = course_info()
        elif choice == 2:
            input_marks(courses, students, marks)
        elif choice == 3:
            show_students(students, courses, marks)
        elif choice == 4:
            show_courses(courses, students, marks)
        elif choice == 5:
            break
        input("\n Press Enter to return to the menu")
main()

# students = [["0", "Khanh Anh", "17", None], ["1", "Tran Anh", "17", None], ["2", "Quang Anh", "17", None]]
# marks = {("0","0") : 100, ("0", "1") : 200, ("0", "2") : 300, ("1","0") : 500, ("1", "1") : 600, ("1", "2") : 800, ("2","0") : 50, ("2", "1") : 20}
# courses = [["0", "Math"], ["1", "Physics"], ["2", "Chemistry"]]