# Module that contains all the core classes for the system

class Person:
    def __init__(self, id, name, email):
        self._id = id
        self._name = name
        self._email = email


class Student(Person):
    def __init__(self, id, name, email):
        super().__init__(id, name, email)

    def __repr__(self):
        return f"{self.id} {self.name} {self.email}"

    def to_dict(self):
        return {
            "id": self._id,
            "name": self._name,
            "email": self._email
        }


class Professor(Person):
    def __init__(self, id, name, email, department):
        super().__init__(id, name, email)
        self._department = department
        # self._assigned_courses = []

    def to_dict(self):
        return {
            "id": self._id,
            "name": self._name,
            "email": self._email,
            "department": self._department
            }
    
    

class Course:
    def __init__(self, code, title, credits, professor):
        self._code = code
        self._title = title
        self._credits = credits
        self._professor = professor
        # self._enrolled_students = [] # list to store enrolled students

    def to_dict(self):
        return{
            "code": self._code,
            "title": self._title,
            "credits": self._credits,
            "professor": self._professor
        }
        