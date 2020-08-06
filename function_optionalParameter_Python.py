#Pi is default argument here.
#Keyword arguments make the code more readable.
def CircleArea (radius, pi = 3.14159):
    Area = pi * pow(radius,2)
    return Area

r = 3
area = CircleArea(3)
print(f'Area of the Circle is : {area} for radius is {r}')