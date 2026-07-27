from database import mycursor
from utils import display_stock


# =====================================
# Customer Purchase History
# =====================================

def view_purchase_history(customer_name, mobile):

    mycursor.execute(
        """
        SELECT odate, name, mobile, pcode, qty, price
        FROM purchase
        WHERE name=%s AND mobile=%s
        ORDER BY odate DESC
        """,
        (customer_name, mobile)
    )

    rows = mycursor.fetchall()

    if not rows:
        print("No purchase history found.")
        return

    print("\n" + "─" * 95)
    print(f"{'DATE':<12}{'NAME':<18}{'MOBILE':<15}{'PCODE':<8}{'QTY':<8}{'PRICE':<10}{'SUBTOTAL'}")
    print("─" * 95)

    total = 0

    for odate, name, mob, pcode, qty, price in rows:

        subtotal = qty * price
        total += subtotal

        print(
            f"{str(odate):<12}"
            f"{name:<18}"
            f"{mob:<15}"
            f"{pcode:<8}"
            f"{qty:<8}"
            f"${price:<9}"
            f"${subtotal}"
        )

    print("─" * 95)
    print(f"{'TOTAL':<71}${total}")
    print("─" * 95)


# =====================================
# Admin Purchase History
# =====================================

def admin_view_all_purchase_history():

    mycursor.execute(
        """
        SELECT odate, name, mobile, pcode, qty, price
        FROM purchase
        ORDER BY odate DESC
        """
    )

    rows = mycursor.fetchall()

    if not rows:
        print("No purchase history found.")
        return

    print("\n" + "─" * 95)
    print(f"{'DATE':<12}{'NAME':<18}{'MOBILE':<15}{'PCODE':<8}{'QTY':<8}{'PRICE':<10}{'SUBTOTAL'}")
    print("─" * 95)

    total = 0

    for odate, name, mob, pcode, qty, price in rows:

        subtotal = qty * price
        total += subtotal

        print(
            f"{str(odate):<12}"
            f"{name:<18}"
            f"{mob:<15}"
            f"{pcode:<8}"
            f"{qty:<8}"
            f"${price:<9}"
            f"${subtotal}"
        )

    print("─" * 95)
    print(f"{'TOTAL SALES':<71}${total}")
    print("─" * 95)