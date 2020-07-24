#Temperture converting from Centigrade to Fahrenheit is :
# F = 9/5 * C + 32
#Question : F = Fahrenheit temperature
# C = the centigrade temperature
#Write a function named fahrenheit that accepts a centigrade temperature as an argument
# function should return the temperature the temperature , converted to Fahrenheit
#Demonstrate the function by calling it in a loop that displays a table of the Centigrade temperature 0 through 20
# and their Fahrenheit equivalents

def fahrenheit(centigrade):
    F = round((1.8*int(centigrade)) + 32, 2)
    print(f'\t{centigrade}\t\t\t\t\t{F}')

print('------------------------------------')
print('Centigrade\t\t\tFahrenheit')
print('------------------------------------')
for i in range(20):
    fahrenheit(i)

print('------------------------------------')

