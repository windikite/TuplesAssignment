orders = [
    ("Alice", "Laptop", 1, "Phone", 2, "PC", 1),
    ("Bob", "Camera", 2, "RC Car", 1),
    ("Jim", "Phone", 4),
    ("Larry", "PC", 1, "Camera", 3),
    ("Billy", "RC Car", 3),
]

def packOrder(products_ordered):
    list_of_orders = []
    order_index = 0
    while order_index < len(products_ordered):
        list_of_orders.append(f"{products_ordered[order_index+1]} {products_ordered[order_index]}")
        order_index += 2
    return list_of_orders

def printOrders():
    orders_to_print = []
    for index, order in enumerate(orders):
        customer, *products_ordered = order
        list_of_orders = packOrder(products_ordered)
        separator = ", "
        new_string = f"Order {index+1}: {customer} - {separator.join(list_of_orders)}"
        orders_to_print.append(new_string)
    separator = "\n"
    string = separator.join(orders_to_print)
    print(string)

printOrders()


