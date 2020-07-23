
#len() function is a general purpose function , so it is not limited to counting the number of characters in a string
# Purpose : To count the number of items in a list
course = 'Python for Beginners'
print(len(course))
print(course)
print(course.upper()) #it creates a new string and return it, it doesn't change our original string
print(course.lower())
print(course.find('P')) #To find the index of the character
print(course.find('o'))
print(course.find('O')) # return -1 , cause we don't have an upper case o anywhere in this string
print(course.find('Beginners')) #return 11 , Beginners -> B starts at index 11

print(course.replace('Beginners', ' absolute Beginners'))

#To check the existence of the character or sequence of characters in string
# use the in operator
#Supposed that we want to know if this string contains the word python
print('Python' in course) #will return boolean value: "Ture or False"