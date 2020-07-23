#Question :

#Write a program that asks the user for the number of mils driven and the gallons of gas used.
#it should calculate the car's MPG and display the result on the screen

#Formula : MPG = Miles driven / Gallons of Gas used

miles_driven  = input('Miles Driven: ')
gallons_of_gas = input ('Gallons of Gas: ')
MPG = round(float(miles_driven) /float(gallons_of_gas) , 2 )
print(' MPG = ' + str(MPG))