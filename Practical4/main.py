import input as inp
import output

def main():
    students = []
    courses = []
    marks = []
    menu_options = ["Enter courses", "Enter students", "Enter marks", "Show courses", "Show students", "Exit"]
    while True:
        choice = output.menu(menu_options)
        if choice == 0:
            courses = inp.input_courses()
        elif choice == 1:
            students = inp.input_students()
        elif choice == 2:
            inp.input_marks(students, courses, marks)
        if choice in (0, 1, 2):
            input("\nPress Enter to return to the menu...")
        elif choice == 3:
            output.show_courses(students, courses, marks)
        elif choice == 4:
            output.show_students(students, courses, marks)
        elif choice == 5:
            break
        

if __name__ == "__main__":
    main()