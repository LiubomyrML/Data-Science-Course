class Chair:
    def __init__(self, color, series_number: str):
        print("Start of creating an Object!")
        self.color = color
        self._series_number  = series_number
        print("End of creating!")
    def greeting(self, model_name: str):
        print(f"HI, {model_name} {self.color} {self._series_number}!")
        print(self)
    def _get_series_number(self):
        return "*"*5 + self._series_number[-2:]

class OfficeChair(Chair):
    def greeting(self, model_name: str):
        print(f"HI, {model_name} {self.color} {self._series_number} {self._get_series_number()}!")

chair1 = Chair(color = "White", series_number = "0001")
chair2 = Chair(color = "Gray", series_number = "0002")
chair3 = Chair(color = "Yellow", series_number = "0003")
chair2.color = "Blue"

officeChair = OfficeChair(color = "Black", series_number = "0004")

chair1.greeting("Bugatti")


from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @abstractmethod
    def greeting(self):
        pass

class Student(Person):
    def greeting(self):
        print(f"Hi, my name is {self.name}, and I am {self.age} years old!")

class Teacher(Person):
    def greeting(self):
        print(f"Hi, my name is {self.name}, and I am {self.age} years old!")

student = Student("Brayden", 15)
student.greeting()
teacher = Teacher("Mrs.Bryant", 67)
teacher.greeting()


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __eq__(self, person2):
        return self.name == person2.name and self.age == person2.age

print(Person("Liubomyr", 14) == Person("Liubomyr", 14))