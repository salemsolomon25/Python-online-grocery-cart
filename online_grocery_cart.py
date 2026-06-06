# Program name: salem_solomon_A8.py A8-Online Grocery Shopping Cart Author: Salem Solomon
total_cart = 0
total_item = 0
total_cost = 0.0

# Dictionaries are set in th beginning to be used later

inventory = {"1": "produce",
             "2": "meat/poultry",
             "3": "Rice/Pasta",
             "4": "bakery",
             "5": "Drinks",
             "c": "Checkout"}
produce_dict = {'1': ['lettuce', 2.5],
                '2': ['apples', 1.25],
                '3': ['brocoli', 3.00],
                '4': ['carrots', 2.95],
                'x': ['return', 'to menu']}
meat_dict = {'1': ['beef', 6.50],
             '2': ['pork', 5.25],
             '3': ['salmon', 8.95],
             '4': ['chicken', 3.95],
             '5': ['hamburger', 4.95],
             'x': ['return', 'to menu']}

rice_dict = {'1': ['basmati', 3.00],
             '2': ['brown rice', 4.25],
             '3': ['spaghetti', 1.75],
             '4': ['penne', 2.25],
             'x': ['return', 'to menu']}
bakery_dict = {'1': ['multigrain bread', 4.50],
               '2': ['croissants', 6.50],
               '3': ['tuscan bread', 3.95],
               '4': ['bagels', 7.95],
               '5': ['baguette', 1.95],
               '6': ['chocolate cake', 8.25],
               'x': ['return', 'to menu']}
drinks_dict = {'1': ['frozen orange juice', 2.95],
               '2': ['apple juice', 2.50],
               '3': ['milk (2%)', 3.95],
               '4': ['Ale', 8.95],
               '5': ['pinot noir', 10.95],
               '6': ['gatorade', 3.50],
               'x': ['return', 'to menu']}
# this function calculates and checks out based on user input
def checkout (cart):
    total = 0.0
    count = 0
    print('Summary of Shopping Cart:')
    print('items\t\t Quantity \t\tcost of items\n')
# iterates through cart and prints it's content
    for c in cart:
        print('{}\t\t{}\t\t{}'.format(c,cart[c][0],cart[c][1]))
        # print(c, cart[c][0], '\t\t\t\t\t', '$ ', cart[c][1], '\n')
        total += cart[c][1]
        count += cart[c][0]
    print('Total items', count, '\t\t', '$', total )
    return count, total

# function displays submenu and prompts for a selection and stores to dictionary cart
def submenu (item_menu):
    option = ''
    while option != 'xX':
        for item in item_menu:
            print(item, item_menu[item][0], item_menu[item][1])
        selection = input('Please enter one of the menu options above or hit x to quit: ')
        if selection in 'xX':
            break
        # validates selection made by user
        if selection not in item_menu:
            selection = input(' Invalid, Please enter one of the menu options above or hit x to quit: ')
        if item_menu[selection][0] in cart:
            cart[item_menu[selection][0]][0] += 1
            cart[item_menu[selection][0]][1] += item_menu[selection][1]
        # adds selected item to cart if not already in there
        else:
            cart[item_menu[selection][0]] = [1, item_menu[selection][1]]

    return selection, cart
# cart is set to 0 to be added to later
cart = {}
while True:
    menu = """
     1 - Produce
     2 - Meat/Poultry
     3 - Rice/Pasta
     4 - Bakery
     5 - Drinks
     c - Checkout
     Select one of the menu options above
    """
    print(menu)
    # prompts the user for category selection
    item = input('Select one of the menu options above: ')
    # validates the users input
    while item not in ('1', '2', '3', '4', '5', 'c'):
        item = input('Invalid input, please try again: ')
    # while loop sets conditions for the function submenu to be called
    while item not in 'c':
        if item == '1':
            sel, cart_count = submenu(produce_dict)
        elif item == '2':
            sel, cart_count = submenu(meat_dict)
        elif item == '3':
            sel, cart_count = submenu(rice_dict)
        elif item == '4':
            sel, cart_count = submenu(bakery_dict)
        elif item == '5':
            sel, cart_count = submenu(drinks_dict)
        if sel in 'xX':
                break
    # checks out the user using the function checkout
    if item in 'c':
        print(cart)
        result = checkout(cart)
        repeat = input('would you like to continue shopping? (y/n) ')
        # calculates the total cart, total item, and total cost
        total_cart += 1
        total_item += result[1]
        total_cost += result[0]
        if repeat in 'yY':
            cart = {}
            continue
        else:
            # displays total cart, total item, and total cost
            print('Total number of carts: ', total_cart, '\n', 'Total number of items', total_item, '\n', 'Total cost of items: $', total_cost)
            break



input("\n\nHit Enter to end program")