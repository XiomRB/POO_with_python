class Course:
    def __init__(self, course_id, name, requesite, min_credit):
        self.course_id = course_id
        self.name = name
        self.requesite = requesite
        self.__min_credit = min_credit
    
    def has_min_credit(self, grade):
        return grade > self.__min_credit