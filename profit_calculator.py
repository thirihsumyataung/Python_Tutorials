#Question: An electronic company sells circuit boards at a 40 percent profit
#If you know the retail price of a circuit board, you can claculate its profit with the following formula:
# Formula : Profit = Retail price * 0.4
# Write a program that asks the user for the retail price of a circuit board, calculate the amount of profit earned
#for that product, and diplays the results on the screen

Retail_price = input('Retail price : ')
Profit = round(float(Retail_price) * 0.4 , 2)
print('Profit : ' + str(Profit))
