from textwrap import dedent

## need to add dedent

# print('hello')

##dictionary, similar to an object
items = {
    "Wings" : 0
}


def welcome():
    message = """
        **************************************
        **    Welcome to the Snakes Cafe!   **
        **    Please see our menu below.    **
        **
        ** To quit at any time, type "quit" **
        **************************************
        """
    print(dedent(message))


def show_menu():
    menu = """
        Appetizers
        ----------
        Wings
        Cookies
        Spring Rolls

        Entrees
        -------
        Salmon
        Steak
        Meat Tornado
        A Literal Garden

        Desserts
        --------
        Ice Cream
        Cake
        Pie

        Drinks
        ------
        Coffee
        Tea
        Unicorn Tears
        """
    print(dedent(menu))

def take_order():
    while True:
        order = input( """
        ***********************************
        ** What would you like to order? **
        ***********************************
        """)
        if order == 'quit':
            break
        
        # update items
        items[order] += 1

        ## when user places an order
        if order in items:
                amount = items[order]

        print(dedent(f"** {amount + 1}1 order of {order} have been added to your meal **"))

def main():
    welcome()
    show_menu()
    take_order()

if __name__ =="__main__":
    main()
