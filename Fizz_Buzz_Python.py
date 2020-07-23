#Fizz Buzz
#if a number is divisilbe by 3 and 5 --> FIZZ BUZZ
#elif a number is divisible by 3 --> FIZZ
#elif a number is divisible by 5 --> BUZZ
#else just a number ( user input )

myFizzBuzzList = []
aString = ''
number = int(input('How many numbers user want to type ? '))

for i in range(number):
    userInput = int(input( ))
    #print(myFizzBuzzList)
    if (userInput%3 == 0) and (userInput%5 == 0):
        aString = 'FIZZ BUZZ'
        #print("Fizz BUZZ")
    elif (userInput%3) == 0:
        aString = 'FIZZ'
        #print(" FIZZ ")
    elif (userInput%5) ==0:
        aString = 'BUZZ'
        #print('BUZZ')
    else:
        aString = str(userInput)
        #print(userInput)

    myFizzBuzzList.append(aString)

print(myFizzBuzzList)