from person import Person
from datetime import date

class Teacher(Person):

    def __init__(self, salary, specialty, start_time):
        self.specialty = specialty
        self.__start_time = start_time
        self.__salary  = salary
    
    def getBasicDetails(self):
        print(f"Profesor: {self.name}, Curso: {self.specialty}")
    
    def canRetire(self):
        years = self.__yearOfService()
        return years >= 30

    def __yearOfService(self):
        today = date.today()
        actual_year = today.year
        return actual_year - self.__start_time