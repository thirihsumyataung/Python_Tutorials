myNames = ["Charcoal", "Nicolas", "Charcoal", "MoJo" , "Nicky", "MoJo", "MoJo", "Charcoal"]
uniques= []

for index in myNames:
    if index not in uniques:
        uniques.append(index)


print(uniques)