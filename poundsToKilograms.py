#Question : Ask a user their weight ( in pounds ) , convert it to kilograms and print on the terminal
#Approach : Pounds to kiograms =  X pounds / 2.2046 = Y KG
#Note : How to round number in Python  ==> supposed that x is a variable , round ( x , 2 )


weight_in_pounds = input('What is user weight in pounds ? ')
weight_in_kilograms = round(int(weight_in_pounds)/2.2046, 2)
print(weight_in_kilograms)
print('User weight in kilogram is : ' + str(weight_in_kilograms))