import math
class Mark():
    def __init__(self, student, course, score):
        self.student = student
        self.course = course
        self.score = math.floor(score * 10) / 10