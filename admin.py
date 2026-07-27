from database import mydb, mycursor
from utils import (
    get_int,
    display_stock,
    product_exists,
    search_products
)

from reports import (
    admin_dashboard,
    reports_menu
)

from history import admin_view_all_purchase_history

def get_stored_password():

    mycursor.execute(
        "SELECT password FROM login LIMIT 1"
    )

    row = mycursor.fetchone()

    return row[0] if row else None

def change_password(current_password):

    old = input("Enter Old Password : ")

    if old != current_password:
        print("Incorrect Password.")
        return current_password

    new = input("Enter New Password : ")

    mycursor.execute(
        "UPDATE login SET password=%s",
        (new,)
    )

    mydb.commit()

    print("Password Changed Successfully.")

    return new

def add_product():

    while True:

        pcode = get_int("Product Code : ")

        if product_exists(pcode):
            print("Product Code Already Exists.")
            continue

        pname = input("Product Name : ")

        quantity = get_int("Quantity : ")

        price = get_int("Price : ")

        mycursor.execute(
            """
            INSERT INTO stock
            VALUES(%s,%s,%s,%s)
            """,
            (
                pcode,
                pname,
                quantity,
                price
            )
        )

        mydb.commit()

        print("Product Added Successfully.")

        if input("Add Another? (y/n): ").lower() != "y":
            break

def update_price():

    pcode = get_int("Product Code : ")

    if not product_exists(pcode):
        print("Product Not Found.")
        return

    new_price = get_int("New Price : ")

    mycursor.execute(
        """
        UPDATE stock
        SET price=%s
        WHERE pcode=%s
        """,
        (
            new_price,
            pcode
        )
    )

    mydb.commit()

    print("Price Updated.")

def restock_product():

    pcode = get_int("Product Code : ")

    if not product_exists(pcode):
        print("Product Not Found.")
        return

    qty = get_int("Quantity To Add : ")

    mycursor.execute(
        """
        UPDATE stock
        SET quantity = quantity + %s
        WHERE pcode=%s
        """,
        (
            qty,
            pcode
        )
    )

    mydb.commit()

    print("Stock Updated.")

def delete_product():

    pcode = get_int("Product Code : ")

    if not product_exists(pcode):
        print("Product Not Found.")
        return

    mycursor.execute(
        "DELETE FROM stock WHERE pcode=%s",
        (pcode,)
    )

    mydb.commit()

    print("Product Deleted.")

def admin_menu():

    password = input("Enter Password : ")

    stored = get_stored_password()

    if password != stored:
        print("Wrong Password.")
        return

    while True:

        print("""
1. Add Product
2. Update Price
3. Restock Product
4. Delete Product
5. Display Products
6. Search Product
7. Dashboard
8. Reports & Analytics
9. Customer Purchase History
10. Change Password
11. Logout
""")

        choice = get_int("Enter Choice : ")

        if choice == 1:
            add_product()

        elif choice == 2:
            update_price()

        elif choice == 3:
            restock_product()

        elif choice == 4:
            delete_product()

        elif choice == 5:
            display_stock()

        elif choice == 6:
            search_products()

        elif choice == 7:
            admin_dashboard()

        elif choice == 8:
            reports_menu()

        elif choice == 9:
            admin_view_all_purchase_history()

        elif choice == 10:
            password = change_password(password)

        elif choice == 11:
            break

        else:
            print("Invalid Choice.")


