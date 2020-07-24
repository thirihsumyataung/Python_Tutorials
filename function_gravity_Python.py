# formula : distance d  = 1/2 * g * t2
# g = 9.8
# t is the amount of time in seconds

# Write a function called fallingDistance that accept the object's falling  tine in seconds as an argument
#The function should return the distance in meters that the object has fallen during time interval
#Demonstrate the method by calling it in a loop that passes the values 1 through 10 as arguments and displays the return value

def fallingDistance(time):
    distance =round( 0.5 * 9.8 * int(time),2)

    print(f'Distance in {time} second is : {distance}')

for i in range(10):
    fallingDistance(i+1)