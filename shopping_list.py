# Python Practices
# Shopping List
# This program asks the user to add an item and then displays the items in the list

shopping_list = []

item1 = input("Enter first item: ")
item2 = input("Enter second item: ")
item3 = input("Enter third item: ")

shopping_list.append(item1)
shopping_list.append(item2)
shopping_list.append(item3)

print("Your shopping list: ")

for item in shopping_list:
    print("-", item)
