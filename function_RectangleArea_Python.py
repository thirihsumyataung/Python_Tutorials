#Question: Write a program that asks the user to enter the width and length of a rectangle,
# and then display the rectangle’s area
#•	getLength – This function should ask the user to enter the rectangle’s length, and then return that value as a double.
#•	getWidth – This method should ask the user to enter the rectangle’s width, and then return that value as a double.
#•	getArea – This method should accept the rectangle’s length and width as arguments, and return the rectangle’s area.
#           The area is calculated by multiplying the length by width.
#•	displayArea – This method should accept the rectangle’s length, width, and area as arguments, and display them in an appropriate message to the screen.

def getLength():
    length = float(input('Enter the length of the Rectangle: '))
    return length
def getWidth():
    width = float(input('Enter the width of the Rectangle: '))
    return width
def getArea(length , width):
    area = round((length * width),2)
    return area
def displayArea(length, width, area):
    print('--------------------------------------------')
    print('Length of the Rectangle is : ' + str(length))
    print('Width of the Rectangle is : ' + str(width))
    print('Area of the Rectangle is : ' + str(area))
    print('--------------------------------------------')


length = getLength()
width = getWidth()
area = getArea(length, width)
displayArea(length, width, area)
