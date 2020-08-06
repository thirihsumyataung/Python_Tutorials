# Question : Write a program to remove the duplicates in a list

myList = [5, 2, 1, 7, 4,9,9,9,9,9, 90, 100, 2, 2, 30, 2, 4, 5, 85,75, 65, 96 ]
uniques = []
for i in myList:
    if i not in uniques:
        uniques.append(i)

print(uniques)