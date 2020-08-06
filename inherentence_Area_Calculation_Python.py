class Area:
    def __init__(self, length , width, height):
        self.length = length
        self.width = width
        self.height = height

    def getLength(self):
        return self.length

    def getWidth(self):
        return self.width

    def display(self):
        print(f'Length is: {self.length} ')
        print(f'Width is: {self.width} ')
        print(f'Length is: {self.height} ')

class Rectangle(Area):

    def areaOfRec(self):
        result = (self.length * self.width * self.height)
        print(result)
        return  result

class Triangle(Area):
    def areaOfRec(self, length, height):
        result = (0.5 * length * height)
        print(result)
        return result

tri = Triangle(13,4,1)
tri.areaOfRec(13, 4  )

rec =Rectangle(3,5,12)
rec.areaOfRec()
rec.display()
