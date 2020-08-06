def add(*arguments):
    total = 0
    for numbers in arguments:
        total = total + numbers
    return total

print(add(35,70,10,25,68,40))