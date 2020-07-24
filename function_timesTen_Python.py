#Question: write a function named timesTen
#function should accept a double argument ,
# and return a double value that is ten times the value of the argument
# call the function anf printout the result

def timesTen(arg):
    value = float (arg) * 10
    print("Ten Times value of userInput is : " + str(value))

value = float(input('User Input is : '))
timesTen(value)


