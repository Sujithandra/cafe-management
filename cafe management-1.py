menu={
    'pasta':40,
    'pizza':50,
    'burger':40,
    'salad':70,
    'coffee':30'
}
print("welcome to our restaurant:")
print("pasta: Rs.40\n pizza: Rs.50\n burger: Rs.40\n salad: Rs.70\n coffee: Rs.30)
order_items=0
item_1=input("enter the name of the item you want to order:")
if item_1 in menu:
    order_item+=menu[item_1]
    print("your item {item-1} has been added to your order")
else:
    print("order item {item-1} is not available")
another_order=input("Do you want to order another item? (yes/no)")
if another_order=="yes":
    item_2=input("enter the name of second item=")
    if item_2 in menu:
        order_items+=menu[item-2]
    else:
        print("order item {item-2}not available")
print("The total amount of items is {order_items}")
