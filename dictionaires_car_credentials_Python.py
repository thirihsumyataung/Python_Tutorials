carInput = input('Enter a car owner name: ')
car = {
    "Joe" : {
        "Car" : "Honda",
        "Model": " 2006",
        "Mileage" : " 1344323523646",
        "Status" : "Used",
        "Condition" : "Old"

   },
    "Jack": {
        "Car": "BMW",
        "Model": " 2020",
        "Mileage": " 7801",
        "Status": "Used",
        "Condition": "Just Like a New"
    },
    "Jay": {
        "Car": "Land Crusier",
        "Model": " 2000",
        "Mileage": " 341778478821921",
        "Status": "Used",
        "Condition": "Old"
    }
}

input = " "
if carInput in car:
    input += str(car.get(carInput," "))

print(input)