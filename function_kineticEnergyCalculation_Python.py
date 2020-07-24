#Write a function named kineticEnergy that accepts an object’s mass (in kilograms) and velocity (in meters per second) as arguments.
# The function should return the amount of kinetic energy that the object has.
# Demonstrate the function by calling it in a program that asks the user to enter values for mass and velocity.

#Formula: KE = ½ mv2 where KE is the kinetic energy , m is the object's mass in kilograms , V is the object's velocity(in meters per second)

def kineticEnergy(mass, velocity):
    KE = round((0.5 * mass * pow(velocity,2)), 2)
    print("Kinetic Energy : KE = " + str(KE))
    return KE

mass = float(input("An object's mass in kilograms: "))
velocity = float(input("The object;s velocity in meters per second: "))
KE = kineticEnergy(mass, velocity)

