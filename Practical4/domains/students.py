import math
import numpy as np

class Student():
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
    
    def __str__(self):
      return f"{self.id} - {self.name}"

    def cal_gpa(self, marks):
        scores = []
        credits = []
        for mark in marks:
            if mark.student is self:
                scores.append(mark.score)
                credits.append(mark.course.credits)
        if not credits:
            return 0.0
        scores = np.array(scores)
        credits = np.array(credits)
        gpa = np.sum(scores * credits) / np.sum(credits)
        gpa = math.floor(gpa * 10) / 10
        return gpa
    
def sort_by_gpa(students, marks):
    gpas = []
    for s in students:
        gpas.append(s.cal_gpa(marks))
    gpas = np.array(gpas)
    order = gpas.argsort()[::-1]
    return [students[i] for i in order]