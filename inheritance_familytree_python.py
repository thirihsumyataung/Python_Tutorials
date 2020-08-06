class Person:
    def __init__(self , name , id):
        self.name = name
        self.id = id

    def getPersonName(self):
        return self.name

    def aStudent(self):
        return False

    def displayStatus(self):
        print(f'{self.name}\n{self.id}')


class Student(Person):
    def __init__(self, name , id, age ):
        self.name = name
        self.age = age
        self.id = id

    def display_student(self):
        print(f'{self.name}\n{self.id}\n{self.age}')
        print (" A student")


class Employee(Person):
    def __init__(self, name, id, age):
        self.name = name
        self.age = age
        self.id = id

    def display(self):
        print(f'{self.name}\n{self.id}\n{self.age}')
        print(" A Employee")


MgMg = Student("Mg Mg", "161152", 26)
MgMg.displayStatus()

MgMg.display_student()
