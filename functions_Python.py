def myFunction():
    print("Hello from My function")

myFunction()

def lastName (firstName):
    print(firstName + " Smith")
fName = input("What is your first name ? ")
lastName(fName)

#arbitary arguments , *args


def kids(kid1, kid2, kid3):
    print(kid1 + " " + kid2 + " " + kid3)
def myKids(*kids):
    print( " The youngest child is : " + kids[2])
kids("Emil", "Katherine","Nora")