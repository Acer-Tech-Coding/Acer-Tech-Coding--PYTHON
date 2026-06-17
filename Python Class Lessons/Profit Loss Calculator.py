actual_cost_price = float(input("Enter the actual cost price: "))
selling_price = float(input("Enter the selling price: "))

amount = selling_price - actual_cost_price

if selling_price > actual_cost_price:
    print("You made a profit of:", "{0}".format(amount))

else:    print("You made a loss of:", "{0}".format(amount))     