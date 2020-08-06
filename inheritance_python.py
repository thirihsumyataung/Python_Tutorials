class Mammals:
    def walk(self):
        print("Walk")


class Dog(Mammals):
    def bark(self):
        print("Bark")

class Cat(Mammals):
    def be_annoying(self):
        print('annoying')

dog1 = Dog()
dog1.walk()
dog1.bark()