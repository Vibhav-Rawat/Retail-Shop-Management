from database import mycursor
from utils import display_stock, get_int
def admin_dashboard():

    print("\n" + "═" * 45)
    print("               ADMIN DASHBOARD")
    print("═" * 45)

    # Total Products
    mycursor.execute("SELECT COUNT(*) FROM stock")
    total_products = mycursor.fetchone()[0]

    # Inventory Value
    mycursor.execute(
        "SELECT IFNULL(SUM(quantity * price),0) FROM stock"
    )
    inventory_value = mycursor.fetchone()[0]

    # Low Stock
    mycursor.execute(
        "SELECT COUNT(*) FROM stock WHERE quantity BETWEEN 1 AND 5"
    )
    low_stock = mycursor.fetchone()[0]

    # Out Of Stock
    mycursor.execute(
        "SELECT COUNT(*) FROM stock WHERE quantity=0"
    )
    out_stock = mycursor.fetchone()[0]

    # Revenue
    mycursor.execute(
        "SELECT IFNULL(SUM(qty*price),0) FROM purchase"
    )
    revenue = mycursor.fetchone()[0]

    # Orders
    mycursor.execute(
        "SELECT COUNT(*) FROM purchase"
    )
    orders = mycursor.fetchone()[0]

    print(f"Total Products       : {total_products}")
    print(f"Inventory Value      : ${inventory_value:,}")
    print(f"Low Stock Items      : {low_stock}")
    print(f"Out Of Stock Items   : {out_stock}")
    print(f"Total Revenue        : ${revenue:,}")
    print(f"Total Orders         : {orders}")

    print("═" * 45)

def revenue_report():

    mycursor.execute(
        "SELECT IFNULL(SUM(qty*price),0) FROM purchase"
    )

    revenue = mycursor.fetchone()[0]

    print(f"\nTotal Revenue : ${revenue:,}")

def inventory_value():

    mycursor.execute(
        "SELECT IFNULL(SUM(quantity*price),0) FROM stock"
    )

    value = mycursor.fetchone()[0]

    print(f"\nInventory Value : ${value:,}")

def best_selling_product():

    mycursor.execute("""
        SELECT
        pcode,
        SUM(qty) AS sold
        FROM purchase
        GROUP BY pcode
        ORDER BY sold DESC
        LIMIT 1
    """)

    row = mycursor.fetchone()

    if row:

        pcode, sold = row

        mycursor.execute(
            "SELECT pname FROM stock WHERE pcode=%s",
            (pcode,)
        )

        name = mycursor.fetchone()

        if name:
            print(f"\nBest Selling Product : {name[0]}")
            print(f"Product Code         : {pcode}")
            print(f"Units Sold           : {sold}")

    else:
        print("No sales found.")

def least_selling_product():

    mycursor.execute("""
        SELECT
        pcode,
        SUM(qty) AS sold
        FROM purchase
        GROUP BY pcode
        ORDER BY sold ASC
        LIMIT 1
    """)

    row = mycursor.fetchone()

    if row:

        pcode, sold = row

        mycursor.execute(
            "SELECT pname FROM stock WHERE pcode=%s",
            (pcode,)
        )

        name = mycursor.fetchone()

        if name:
            print(f"\nLeast Selling Product : {name[0]}")
            print(f"Product Code          : {pcode}")
            print(f"Units Sold            : {sold}")

    else:
        print("No sales found.")

def low_stock_report():

    mycursor.execute(
        "SELECT * FROM stock WHERE quantity BETWEEN 1 AND 5"
    )

    rows = mycursor.fetchall()

    if rows:
        display_stock(rows)
    else:
        print("No low stock products.")

def out_of_stock_report():

    mycursor.execute(
        "SELECT * FROM stock WHERE quantity=0"
    )

    rows = mycursor.fetchall()

    if rows:
        display_stock(rows)
    else:
        print("No out of stock products.")

def reports_menu():

    while True:

        print("""
1. Revenue Report
2. Inventory Value
3. Best Selling Product
4. Least Selling Product
5. Low Stock Report
6. Out Of Stock Report
7. Back
""")

        choice = get_int("Enter Choice : ")

        if choice == 1:
            revenue_report()

        elif choice == 2:
            inventory_value()

        elif choice == 3:
            best_selling_product()

        elif choice == 4:
            least_selling_product()

        elif choice == 5:
            low_stock_report()

        elif choice == 6:
            out_of_stock_report()

        elif choice == 7:
            break

        else:
            print("Invalid Choice")

