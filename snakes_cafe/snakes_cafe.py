from textwrap import dedent

## need to add dedent

# print('hello')

##dictionary, similar to an object
items = {
    "Wings" : 0,
    "Cookies" : 0,
    "Spring Rolls" : 0,
    "Salmon" : 0,
    "Steak" : 0,
    "Meat Tornado" : 0,
    "A Literal Garden" : 0,
    "Ice Cream" : 0,
    "Cake" : 0,
    "Pie" : 0,
    "Coffee" : 0,
    "Tea" : 0,
    "Unicorn Tears" : 0,
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
    print(dedent("""
    ***********************************
    ** What would you like to order? **
    ***********************************
    """))
    while True:
        order=input()
        if order == 'quit':
            break
        
        # update items
        # items[order] += 1

        ## when user places an order           
        if order in items:
                amount = items[order]
                if amount ==0:
                    print(f"\n** {amount + 1} order of {order} have been added to your meal **\n")
                    items[order]+=1
                if amount >=1:
                    print(f"\n** {amount + 1} orders of {order} have been added to your meal **\n")
                    items[order]+=1
                


def main():
    welcome()
    show_menu()
    take_order()

if __name__ =="__main__":
    main()
