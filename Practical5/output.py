import curses
from domains import sort_by_gpa
UP_KEYS = (curses.KEY_UP, 450)
DOWN_KEYS = (curses.KEY_DOWN, 456)        
ENTER_KEYS = (curses.KEY_ENTER, 10, 13, 459) 
def draw_header(stdscr, title):
    stdscr.addstr(0, 0, title, curses.A_BOLD)


def draw_screen(stdscr, options, selected):
    for i in range(len(options)):
        if i == selected:
            attr = curses.A_REVERSE
        else:
            attr = curses.A_NORMAL
        stdscr.addstr(2 + i, 2, options[i], attr)


def choosing(stdscr, options, title):
    curses.curs_set(0)
    selected = 0
    while True:
        stdscr.clear()
        draw_header(stdscr, title)
        draw_screen(stdscr, options, selected)
        stdscr.refresh()
        key = stdscr.getch()
        if key in UP_KEYS and selected > 0:
            selected -= 1
        elif key in DOWN_KEYS and selected < len(options) - 1:
            selected += 1
        elif key in ENTER_KEYS:
            return selected


def menu(options, title="Students Management Program"):
    return curses.wrapper(choosing, options, title)


def find_score(marks, student, course):
    for mark in marks:
        if mark.student is student and mark.course is course:
            return mark.score
    return None


def show_students(students, courses, marks):
    sorted_students = sort_by_gpa(students, marks)

    options = []
    for i in range(len(sorted_students)):
        s = sorted_students[i]
        options.append(f"{i + 1}. {s.name} (GPA: {s.cal_gpa(marks)})")
    options.append("Back to main menu")

    while True:
        choice = menu(options, "Students (sorted by GPA)")
        if choice == len(options) - 1:
            break

        student = sorted_students[choice]
        lines = []
        for i in range(len(courses)):
            score = find_score(marks, student, courses[i])
            if score is None:
                score = "N/A"
            lines.append(f"{i + 1}. {courses[i].name}: {score}")
        lines.append(f"GPA: {student.cal_gpa(marks)}")
        lines.append("Back to students list")
        menu(lines, f"Marks of {student.name}")


def show_courses(students, courses, marks):
    options = []
    for i in range(len(courses)):
        options.append(f"{i + 1}. {courses[i].name} ({courses[i].credits} credits)")
    options.append("Back to main menu")

    while True:
        choice = menu(options, "Courses")
        if choice == len(options) - 1:
            break

        course = courses[choice]
        lines = []
        for i in range(len(students)):
            score = find_score(marks, students[i], course)
            if score is None:
                score = "N/A"
            lines.append(f"{i + 1}. {students[i].name}: {score}")
        lines.append("Back to courses list")
        menu(lines, f"Marks in {course.name}")