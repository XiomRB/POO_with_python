from abc import ABC, abstractmethod
class Person:
    
    def __init__(self, person_id=1, name="", address="", email="", phone_number=""):
        self.person_id = person_id
        self.name = name
        self.address = address
        self.email = email
        self.phone_number = phone_number
    
    @abstractmethod
    def getBasicDetails(self):
        pass

