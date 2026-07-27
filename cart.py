from datetime import date
from database import mydb, mycursor
from utils import stock_status


# ================================
# Add Item To Cart
# ================================

def add_to_cart(cart):

    pcode = int(input("Enter Product Code : "))

    mycursor.execute(
        "SELECT pname, quantity, price FROM stock WHERE pcode=%s",
        (pcode,)
    )

    row = mycursor.fetchone()

    if row is None:
        print("Product not found.")
        return

    pname, available_qty, price = row

    if available_qty == 0:
        print("This product is OUT OF STOCK.")
        return

    qty = int(input("Enter Quantity : "))

    if qty > available_qty:
        print(f"Only {available_qty} item(s) available.")
        return

    for item in cart:

        if item["pcode"] == pcode:

            if item["qty"] + qty > available_qty:
                print(f"Only {available_qty} item(s) available.")
                return

            item["qty"] += qty
            print("Quantity Updated In Cart.")
            return

    cart.append({
        "pcode": pcode,
        "pname": pname,
        "qty": qty,
        "price": price
    })

    print("Item Added To Cart.")

def view_cart(cart):

    if not cart:
        print("Your cart is empty.")
        return cart

    while True:

        print("\n" + "─"*80)
        print(f"{'ITEM':<6}{'PCODE':<8}{'PRODUCT NAME':<25}{'QTY':<8}{'PRICE':<10}{'SUBTOTAL'}")
        print("─"*80)

        total = 0

        for idx, item in enumerate(cart, 1):

            subtotal = item["qty"] * item["price"]
            total += subtotal

            print(
                f"{idx:<6}"
                f"{item['pcode']:<8}"
                f"{item['pname']:<25}"
                f"{item['qty']:<8}"
                f"${item['price']:<9}"
                f"${subtotal}"
            )

        print("─"*80)
        print(f"{'TOTAL':<57}${total}")
        print("─"*80)

        print("""
1. Remove Item
2. Back
""")

        ch = int(input("Enter Choice : "))

        if ch == 1:

            item_no = int(input("Enter Item Number : "))

            if 1 <= item_no <= len(cart):

                removed = cart.pop(item_no-1)

                print(removed["pname"], "removed.")

            else:
                print("Invalid Item Number.")

            if not cart:
                print("Cart Empty.")
                break

        elif ch == 2:
            break

        else:
            print("Invalid Choice.")

    return cart

def checkout(cart, customer_name, mobile):

    if not cart:
        print("Your cart is empty.")
        return

    total = 0

    for item in cart:
        total += item["qty"] * item["price"]

    print("\nTotal Amount :", total)

    confirm = input("Proceed To Payment? (y/n): ")

    if confirm.lower() != "y":
        return

    input("Enter Your Mobile Number To Pay : ")

    today = date.today()

    for item in cart:

        mycursor.execute(
            """
            INSERT INTO purchase
            VALUES(%s,%s,%s,%s,%s,%s)
            """,
            (
                today,
                customer_name,
                mobile,
                item["pcode"],
                item["qty"],
                item["price"]
            )
        )

        mycursor.execute(
            """
            UPDATE stock
            SET quantity = quantity-%s
            WHERE pcode=%s
            """,
            (
                item["qty"],
                item["pcode"]
            )
        )

    mydb.commit()

    cart.clear()

    print("""
────────────────────────────────────
Payment Successful
Thank You For Shopping With Us
Visit Again!
────────────────────────────────────
""")


def cart_reserved_qty(cart, pcode):

    total = 0

    for item in cart:

        if item["pcode"] == pcode:
            total += item["qty"]

    return total

