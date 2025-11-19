menu = {
    'veg': {
        'pasta': 40,
        'pizza': 50,
        'veg-burger': 40,
        'salad': 70,
        'coffee': 30
    },
    'non-veg': {
        'chicken-burger': 100,
        'chicken-pizza': 100
    }
}

print("Welcome to our restaurant!")

Item = input("Enter 'veg' for veg items\nEnter 'non-veg' for non-veg items\nEnter 'none' for no order\nYour choice: ").lower()

if Item == "veg":
    print("""
Veg Menu:
    pasta : 40
    pizza : 50
    veg-burger : 40
    salad : 70
    coffee : 30
    """)

elif Item == "non-veg":
    print("""
Non-Veg Menu:
    chicken-burger : 100
    chicken-pizza  : 100
    """)

else:
    print("No order")
    exit()

order_items = 0

item_1 = input("Enter the name of the item you want to order: ").lower()

if item_1 in menu[Item]:
    order_items += menu[Item][item_1]
    print(f"Your item '{item_1}' has been added to your order.")
else:
    print(f"Item '{item_1}' is not available.")

another_order = input("Do you want to order another item? (yes/no): ").lower()

if another_order == "yes":
    item_2 = input("Enter the name of the second item: ").lower()
    if item_2 in menu[Item]:
        order_items += menu[Item][item_2]
        print(f"Your item '{item_2}' has been added.")
    else:
        print(f"Item '{item_2}' is not available.")

print(f"The total bill amount is: Rs.{order_items}")


