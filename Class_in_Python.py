
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print(f'Point move to : {self.x} , {self.y}')

    def draw(self):
        print(f'Draw to {self.x} , {self.y}')


point1 = Point(100, 200)
#print(point1.x) # x coordinate of point1 is 100
print(point1.x)
point1.draw()

point1.draw()
point1.move()
