numbers = [5, 2, 1, 7, 4,9,9,9,9,9 ]
numbers.insert(0, 10) # 0 is the index of the value we want to insert , 10 is the value we want to insert
numbers.append(20)
numbers.remove(1) # to remove the number
# to empty the list  numbers.clear()
numbers.pop() # to pop the last number of the list

#To get the index of the number
print(numbers.index(2))
print(numbers)
print(50 in numbers) # to check if 50 is in numbers list

#To count the numbers in "numbers list"
print( numbers.count(9))

#To sort the list
numbers.sort() #ascending order
print(numbers)

numbers.reverse() #decending order
print(numbers)

#To copy the list
numbers.append(50)
numbers_copy = numbers.copy()
numbers.append(30)
print(numbers_copy)
print(numbers)