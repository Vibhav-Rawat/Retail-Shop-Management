from database import mycursor


# ================================
# Input Validation
# ================================

def get_int(prompt):
    """Safely read an integer from input."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


# ================================
# Stock Status
# ================================

def stock_status(quantity):
    if quantity == 0:
        return "OUT OF STOCK"
    elif quantity <= 5:
        return "LOW STOCK"
    else:
        return "IN STOCK"


# ================================
# Product Exists
# ================================

def product_exists(pcode):
    mycursor.execute(
        "SELECT * FROM stock WHERE pcode=%s",
        (pcode,)
    )
    return mycursor.fetchone() is not None


# ================================
# Display Stock
# ================================

def display_stock(rows=None):

    if rows is None:
        mycursor.execute("SELECT * FROM stock")
        rows = mycursor.fetchall()

    if not rows:
        print("No products found.")
        return rows

    print("\n" + "─" * 78)
    print(f"{'PCODE':<8}{'PRODUCT NAME':<28}{'QUANTITY':<12}{'PRICE':<10}{'STATUS'}")
    print("─" * 78)

    for pcode, pname, qty, price in rows:
        print(
            f"{pcode:<8}"
            f"{pname:<28}"
            f"{qty:<12}"
            f"{price:<10}"
            f"{stock_status(qty)}"
        )

    print("─" * 78)

    return rows


# ================================
# Search Products
# ================================

def search_products():

    keyword = input("Enter Product Name or Product Code: ")

    if keyword.isdigit():

        mycursor.execute(
            "SELECT * FROM stock WHERE pcode=%s",
            (int(keyword),)
        )

    else:

        mycursor.execute(
            "SELECT * FROM stock WHERE pname LIKE %s",
            ("%" + keyword + "%",)
        )

    rows = mycursor.fetchall()

    if rows:
        display_stock(rows)
    else:
        print("No matching products found.")