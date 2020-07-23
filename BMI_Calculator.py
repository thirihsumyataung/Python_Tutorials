#Body Mass Index
# Formula : BMI = kg / m2
# BMI of 25.0 or more is overweight
# Healthy range is 18.5 to 24.9
# Obesity is 30 or greater

print('--------------------------------')
feet = input('Feet : ')
feet_into_inches = int(feet) * 12
inches = input('Inches : ')
input_inches = int(inches)
total_inches = feet_into_inches + int(inches)

print("Total inches : " + str(total_inches))
cm = total_inches * 2.54
meter = cm * 0.01

weight_in_pounds = input('What is user weight in pounds ? ')
weight_in_kilograms = round(int(weight_in_pounds)/2.2046, 2)
#print(weight_in_kilograms)
print('User weight in kilogram is : ' + str(weight_in_kilograms))
print('--------------------------------')
BMI = round(weight_in_kilograms / (meter ** 2), 2)
print("Your BMI is : " + str(BMI))
print('--------------------------------')
print('According to the BMI categories: ')
if BMI < 18.5 :
    print('   Your BMI is Underweight')
elif BMI >= 18.5 or BMI <=24.9 :
    print('     Your BMI is Normal Weight')
elif BMI >=25.0 or BMI <=29.9:
    print('     Your BMI is Overweight')
else :
    print('     Your BMI is Obesity ')

print('--------------------------------')
