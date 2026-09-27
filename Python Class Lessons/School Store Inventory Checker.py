items = ["pencil", "eraser", "notebook", "pencil", "sharpner"]
stock_count = [12, 0, 8, 5, 3]

inventory = {item: count for item, count in zip(items, stock_count)}
print("Current Inventory:", inventory)

in_stock_items = {item: count for item, count in inventory.items() if count > 0}
print("Items in Stock:", in_stock_items)

chosen_item = input("Enter the item you want to buy: ")

if chosen_item not in inventory or inventory[chosen_item] == 0:
    print(f"Sorry, {chosen_item} is out of stock.")
    exit()   

prices = [10, 5, 20, 15, 8] 
tax_rate = 18

total_price = list(map(lambda price: price + (price * tax_rate / 100), prices))
print("Total prices with tax:", total_price)

item_index = items.index(chosen_item)
chosen_item_price = total_price[item_index]
print(f"The total price for {chosen_item} including tax is: {chosen_item_price}")

inventory[chosen_item] = inventory[chosen_item] - 1
print(f"Thank you for your purchase! You bought a/an {chosen_item} for {chosen_item_price}.")
print(f"Updated Inventory after purchasing {chosen_item}: {inventory}")

print("")
print("===== SCHOOL STORE INVENTORY CHECKER =====")