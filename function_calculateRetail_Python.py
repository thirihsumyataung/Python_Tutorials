#Question : Write a program that asks the user to enter an item's wholesale cost and its markup percentage.
#then display the items retail price
# •	If an item’s wholesale cost is 5.00 and its markup percentage is 100 percent, then the item’s retail price is 10.00
# •	If an item’s wholesale cost is 5.00 and its markup percentage is 50 percent, then the item’s retail price is 7.50
# function named calculateRetail that receives the wholesale cost and the markup percentage as arguments,
# and returns the retail price of the item.

#Formula: Retail = cost + ( markup percentage * cost)
def calculateRetail(wholesaleCost , markupPercentage):
    markupPercentage = markupPercentage/100
    retail = round (wholesaleCost + (wholesaleCost * markupPercentage), 2)
    return retail
def markupAmount ( wholesaleCOst , markupPercentage):
    markupPercentage = markupPercentage/100
    markup = round((wholesaleCOst * markupPercentage),2)
    return markup
print('---------------------------------------')
print('\tCost Percent Markup Retail Price')
print('\t\tRequired Data Entry')
print('---------------------------------------')
user_retail = float(input('Retail Price: '))
user_markup_Percentage = float(input('Markup Percentage: '))
retail = calculateRetail(user_retail , user_markup_Percentage)
markup_Amount = markupAmount(user_retail, user_markup_Percentage)
print('---------------------------------------')
print('\t\tCalculated Results')
print('---------------------------------------')
print('Calculated Markup Amount is : ' + str(markup_Amount))
print('Calculated Retail Price is : ' + str(retail))
print('---------------------------------------')
