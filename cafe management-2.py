menu={'veg':
{
    'pasta':40,
    'pizza':50,
    'veg-burger':40,
    'salad':70,
    'coffee':30'
}
    'Non-veg':
    {
        'chicken-burger':100,
        'chicken-pizza':100,
    }
}
print("welcome to our restaurant:")
Item=input("enter veg for vegItem \n enter Non-veg  for non-veg enter None for no order")
if Item="veg":
    println("""
veg:
    pasta:40
    pizza:50,
    veg-burger:40,
    salad:70,
    coffee:30,
    """)
    
elif item="non-veg":
    print("""
    Non-veg:
        chicken-burger:100,
        chicken-pizza:100,
        """)
else :
    ("No order")
order_items=0
item_1=input("enter the name of the item you want to order:")
if item_1 in menu["Item"]:
    order_item+=(menu["Item"]["item_1"])
    print("your item {item-1} has been added to your order")
else:
    print("order item {item-1} is not available")
another_order=input("Do you want to order another item? (yes/no)")
if another_order=="yes":
    item_2=input("enter the name of second item=")
    if item_2 in menu:
        order_items+=(menu["item"]["item-2"])
    else:
        print("order item {item-2}not available")
print("The total amount of items is {order_items}")

