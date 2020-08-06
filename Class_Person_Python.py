class Person:
    def __init__(self,name):
        self.name = name

    def talk(self):
        print(self.name + ' is talking ')


person1 = Person("John")
person1.talk()
name1 = Person("Bob Smith")
name1.talk()
