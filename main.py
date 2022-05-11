# from rich.console import Console
# console = Console()


orders = [{
        'order_no': 1234,
        'items': [['s', 5,6,2,11,660],['n', 3,2,1,6.5,39]]
        }]


def calct(ftype, width, height, qty):
    if ftype == 'n':
        rate = 6.5
        sqft = width*height
        amount = 6.5*sqft*qty
        return ftype, width, height, sqft, qty, rate, amount 
    elif ftype == 's':
        rate = 11
        sqft = width*height
        amount = sqft*11*qty
        return ftype, width, height, sqft, qty, rate, amount 
    else:
        return 'Error in input'

def add_order():
    ftype = input("T :")
    width = float(input("W : "))
    height = float(input("H : "))
    qty = int(input("Q :"))
    data = calct(ftype, width, height, qty)
    item = [ data[0], data[1], data[2], data[3], data[4], data[5], data[6]]
    return item

def gen_order():
    order = {}
    order_no = int(input("Order no : "))
    flag = ''
    items = []
    while flag != 'q':
        item = add_order()
        items.append(item)
        flag = input("Done ? (q to done or enter to continue) ")

    order['order_no'] = order_no
    order['items'] = items
    orders.append(order)
    

q = ''

while q != 'q':
    print("Hare Krishna")
    gen_order()
    import os
    os.system('cls')
    print(orders)
    q = input("Press enter to add new item (q to quit) :")
