numbers = [8, 9, 30, 5, 9, 200]
max_number = numbers[0]

for i in numbers:
    if i > max_number :
        max_number = i


print(numbers)
print('The largest number in list is : ' + str(max_number))