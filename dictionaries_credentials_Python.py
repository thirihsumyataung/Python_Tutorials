
input = input('Type "Charcoal" or "Water" or "Air" to know the character(Attention: Case Sensitive) : ')

credentials = {
    "Charcoal" : {
        "color" : "dark",
        "smell" : "None",
        "Usage" : "To set up the fire"
    },

    "Water":{
        "color": "None",
        "smell" : "None",
        "Usage" : "To hydrate the body and plant the tree"
    },

    "Air" : {
        "color" : "None",
        "Smell" : "which depends on enviorment",
        "Usage" : "H2O"

    }
}

userInput = " "
if input in credentials:
    userInput += str(credentials.get(input," "))

print(userInput)
