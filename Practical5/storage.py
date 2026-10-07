import os
import zipfile
from domains import Student, Course, Mark

FILES = ["students.txt", "courses.txt", "marks.txt"]
ARCHIVE = "students.dat"

def find_by_id(items, item_id):
    for item in items:
        if item.id == item_id:
            return item
    return None

def save_data():
    with zipfile.ZipFile(ARCHIVE, "w", zipfile.ZIP_DEFLATED) as z:
        for name in FILES:
            if os.path.exists(name):
                z.write(name)
    for name in FILES:
        if os.path.exists(name):
            os.remove(name)
def load_data(students, courses, marks):
    if not os.path.exists(ARCHIVE):
        return
    with zipfile.ZipFile(ARCHIVE, "r") as z:
        z.extractall()
    read_students(students)
    read_courses(courses)
    read_marks(students, courses, marks)

def read_students(students):
    if not os.path.exists("students.txt"):
        return
    with open("students.txt", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            id, name, dob = line.split("|")
            students.append(Student(id, name, dob))

def read_courses(courses):
    if not os.path.exists("courses.txt"):
        return
    with open("courses.txt", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            id, name, credits = line.split("|")
            courses.append(Course(id, name, int(credits)))

def read_marks(students, courses, marks):
    if not os.path.exists("marks.txt"):
        return
    with open("marks.txt", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            sid, cid, score = line.split("|")
            s = find_by_id(students, sid)
            c = find_by_id(courses, cid)

            marks.append(Mark(s, c, float(score)))
