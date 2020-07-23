userInput_list = []
numbers = int(input('How many numbers user want to type in List ? '))

#For loop to ask the userinput until it reaches the numbers of input entered by user
for count in range(numbers):
    userInput = int(input())
    userInput_list.append(userInput)

print(userInput_list)

max = userInput_list[0]
min = userInput_list[0]
#for loop to find max and min in userInput list
for i in userInput_list:
    if i > max:
        max = i
    elif i < min :
        min = i

print('Maximum number in user given list is: ' + str(max))
print('Minimum number in user given list is: ' + str(min))




