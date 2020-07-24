#Distance = speed * time
# function named distance that accepts a vehicle's speed and time as arguments and
#returns the distance thevehicle has travelled.

def distance ( speed , time ):
    distance = round((float(speed) * int(time)), 2)
    print(f'{time}\t\t\t\t{distance}')
    return distance

time = int(input("User travelled Time :  "))
speed = float(input("Vehicle's speed : "))
print('------------------------------------')
print('Time\t\t\tDistance')
print('------------------------------------')
for t in range(time):
    distance(speed, t)

vehicleTravelled = str(distance(speed,time))
print("The distance that vehicle has travelled is : " + vehicleTravelled)
