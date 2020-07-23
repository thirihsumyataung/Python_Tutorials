list = [9, 100, 89, 8, 4, 3, 2, 5, 6, 7, 1]
min = list[0]

for numbers in list :
    if numbers < min:
        min = numbers

print(list)
print("The minimun number in a given list is: " + str(min))