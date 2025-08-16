from person import Person

class Student(Person):
    def __init__(self, parent_name, parent_contact, status):
        self.parent_name = parent_name
        self.parent_contact = parent_contact
        self.__status = status
    
    def getBasicDetails(self):
        print(f"Estudiante: {self.name}")
        self.getTutorDetails()

    def getTutorDetails(self):
        print(f"Nombre tutor: {self.parent_name}")
        print(f"Contancto: {self.parent_contact}")