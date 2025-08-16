class Grade:
    def __init__(self, grade_id, grade, student, course):
        self.grade_id = grade_id
        self.grade = grade
        self.student = student
        self.course = course
    

    def passed_course(self):
        has_min_credit = self.course.has_min_credit(self.grade)
        if has_min_credit:
            print(f"{self.student.name} aprobó {self.course.name}")
        else:
            print(f"{self.student.name} no aprobó {self.course.name}")
    