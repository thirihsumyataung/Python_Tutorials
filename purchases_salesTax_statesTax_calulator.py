#Ask the user to enter the amount of the purchase
#Compute the state and county sales tax
#Supposed that the state sales tax is 4% , and the county sales tax is 2%
#Program should display the amount of the purchase, the state sales tax, the county sales tax, the total sales tax
# and the total of the sale (which is the sum of the amount of the purchase plus the total sales tax

print('*********************************')
purchase = input("Total purchase: ")
state_sales_tax = round(float(purchase) * 0.04, 2)
county_sales_tax = round(float(purchase) * 0.02, 2)
total_sales_tax = state_sales_tax + county_sales_tax
total_of_the_sales = round(float(purchase)+ total_sales_tax, 2)
print("The amount of the purchase is : " + purchase)
print('State sales tax is : ' + str(state_sales_tax))
print('County sales tax is : ' + str(county_sales_tax))
print('Total sales tax is : ', total_sales_tax)
print('Total of the sales is :', total_of_the_sales)
print('*********************************')
