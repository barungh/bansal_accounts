from rich.console import Console

orders = [
        {
        'order_no': 1234,
        'items': [['s', 5,6,2,11,660],['n', 3,2,1,6.5,39]]
        },
        {
        'order_no': 1133,
        'items': [['s', 5,6,2,11,660],['n', 3,2,1,6.5,39]]
        }
        ]

#E2AEDD
#B81365
#BFAB25
#FAF9F9
#FF6700
#3DFAFF
#FF331F
#80ED99
#DC6ACF


def order_print(orders):
    gtotal = 0
    from rich.theme import Theme

    custom_theme = Theme({
        "t" : "#b81365",
        "on": "#EBCBF4",
        "dm": "#dc6acf",
        "q": "#ff6700",
        "rm": "#80ed99",
        "a": "#ff331f",
        "tt": "#3dfaff"
    })
    
    console = Console(theme=custom_theme)
    
    for i in orders:
        o_n = i['order_no']
        items = i['items']
        for i in items:
            gtotal = gtotal + i[-1]
            console.print(f'[on]Order No.[/on] {o_n} [t]Type:[/t] {i[0].upper()} [dm]Dimension:[/dm] {i[1]}x{i[2]} [q]Qty:[/q] {i[3]} [rm]Rate:[/rm] {i[4]} [a]Amount:[/a] {i[-1]}')
        
    console.print("[tt]Total[/tt]", gtotal)





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
    # print("Hare Krishna")
    import os
    os.system('cls')
    order_print(orders)
    gen_order()
    # print(orders)
    q = input("Press enter to add new item (q to quit) :")
