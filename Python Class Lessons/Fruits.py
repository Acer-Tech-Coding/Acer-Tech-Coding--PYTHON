basket1 = {"apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"}
basket2 = {"banana", "kiwi", "grapes", "pear", "peach", "banana", "mango"}
print("Basket 1 - ", basket1)
print("Basket 2 - ", basket2)


basket1.add("papaya")
print("Basket 1 after adding papaya - ", basket1)

common_fruits = basket1.intersection(basket2)
print("Common fruits in both baskets - ", common_fruits)

import array as arr
fruit_counts = arr.array('i', [3, 5, 2, 4])
print("Fruit counts - ", fruit_counts)

fruit_counts.insert(0, 1)  # Insert 1 at the beginning
print("Fruit counts after insertion - ", fruit_counts)

count_of_4 = fruit_counts.count(4)
print("Count of 4 in fruit counts - ", count_of_4)

fruit_counts.reverse()
print("Fruit counts after reversing - ", fruit_counts)  

print("")
print("===== CLASS FRUIT BASKET ORGANIZER =====")
print("This program will help you organize your fruit basket.")
print("Basket 1:", basket1)
print("Basket 2:", basket2)
print("Shared fruits between both baskets:", common_fruits)
print("Fruit counts in the basket:", fruit_counts)
print("===============================================")
