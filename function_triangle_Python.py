def triangle_area(length, width):
    area = 0.5 * length * width
    print("Area of the Triangle is : " + str(area))

length = float(input('Length of the triangle : '))
width = float(input('Width of the triangle: '))
triangle_area(length, width)