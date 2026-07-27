from utils import get_int, display_stock, search_products
from cart import add_to_cart, view_cart, checkout
from history import view_purchase_history


def customer_menu():

    print("─────────── Welcome ───────────")

    customer_name = input("Enter Your Name : ")
    mobile = input("Enter Your Mobile Number : ")

    cart = []

    while True:

        print("""
1. See All Available Items
2. Search Product
3. Add Item To Cart
4. View Shopping Cart
5. Payment Section
6. Purchase History
7. Exit
""")

        choice = get_int("Enter Your Choice : ")

        if choice == 1:

            display_stock()

        elif choice == 2:

            search_products()

        elif choice == 3:

            add_to_cart(cart)

        elif choice == 4:

            cart = view_cart(cart)

        elif choice == 5:

            checkout(cart, customer_name, mobile)

        elif choice == 6:

            view_purchase_history(customer_name, mobile)

        elif choice == 7:

            break

        else:

            print("Invalid Choice.")