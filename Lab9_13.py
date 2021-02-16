class ItemToPurchase:
    def __init__(self, name='none', price=0, quantity=0, description='none'):
        self.item_name = name
        self.item_description = description
        self.item_price = price
        self.item_quantity = quantity

    def print_item_description(self):
        print('{}: {}'.format(self.item_name, self.item_description))


class ShoppingCart:
    def __init__(self, customer_name='none', current_date='January 1, 2016', cart_items=[]):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items

    def add_item(self, itemToPurchase):
        self.cart_items.append(itemToPurchase)

    def remove_item(self, itemName):
        to_remove_item = False

        for item in self.cart_items:
            if item.item_name == itemName:
                self.cart_items.remove(item)
                to_remove_item = True
                break

        if not to_remove_item:
            print('Item not found in the cart. Nothing removed.')

    def modify_item(self, itemToPurchase):
        to_modify_item = False
        for i in range(len(self.cart_items)):
            if self.cart_items[i].item_name == itemToPurchase.item_name:
                to_modify_item = True
                self.cart_items[i].item_quantity = itemToPurchase.item_quantity
                break
        if not to_modify_item:
            print('Item not found in the cart. Nothing modified.')

    def get_num_items_in_cart(self):
        num_items = 0
        for item in self.cart_items:
            num_items = num_items + item.item_quantity
        return num_items

    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            cost = (item.item_quantity * item.item_price)
            total_cost += cost
        return total_cost

    def print_total(self):
        total_cost = self.get_cost_of_cart()
        if total_cost == 0:
            print('SHOPPING CART IS EMPTY')
        else:
            print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))
            print('Number of Items: {}\n'.format(self.get_num_items_in_cart()))
            for item in self.cart_items:
                total = item.item_price * item.item_quantity
                print('{} {} @ ${} = ${}'.format(item.item_name, item.item_quantity, item.item_price, total))

            print('\nTotal: ${}'.format(total_cost))

    def print_descriptions(self):
        if len(self.cart_items) == 0:
            print('SHOPPING CART IS EMPTY')
        else:
            print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))
            print('\nItem Descriptions')
            for item in self.cart_items:
                item.print_item_description()


def print_menu(ShoppingCart):
    while True:
        print('MENU')
        print('a - Add item to cart')
        print('r - Remove item from cart')
        print('c - Change item quantity')
        print('i - Output items\' descriptions')
        print('o - Output shopping cart')
        print('q - Quit\n')

        menu_op = input('Choose an option:\n')

        if menu_op == 'q':
            break
        elif menu_op == 'a':
            print('ADD ITEM TO CART')
            new_item_name = input('Enter the item name:\n')
            new_item_des = input('Enter the item description:\n')
            new_item_price = int(input('Enter the item price:\n'))
            new_item_num = int(input('Enter the item quantity:\n'))
            add_to_cart = ItemToPurchase(new_item_name, new_item_price, new_item_num, new_item_des)
            ShoppingCart.add_item(add_to_cart)
        elif menu_op == 'r':
            print('REMOVE ITEM FROM CART')
            remove_item_name = input('Enter name of item to remove:\n')
            ShoppingCart.remove_item(remove_item_name)
        elif menu_op == 'c':
            print('CHANGE ITEM QUANTITY')
            item_name_change = input('Enter the name of the item :\n')
            num = int(input('Enter the new quantity :\n'))
            change_item_qty = ItemToPurchase(item_name_change, 0, num)
            ShoppingCart.modify_item(change_item_qty)
        elif menu_op == 'i':
            print('OUTPUT ITEMS\' DESCRIPTIONS')
            ShoppingCart.print_descriptions()
        elif menu_op == 'o':
            print('OUTPUT SHOPPING CART')
            ShoppingCart.print_total()


if __name__ == "__main__":
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    new_cart = ShoppingCart(customer_name, current_date)
    print_menu(new_cart)