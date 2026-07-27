from database import setup_database
from utils import get_int
from admin import admin_menu
from customer import customer_menu

# Create database and tables
setup_database()

print(r"""
───────────────── ✦ RETAIL SHOP MANAGEMENT SYSTEM ✦ ─────────────────
""")

while True:
    print("""
1. Admin
2. Customer
3. Exit
""")

    choice = get_int("Enter Your Choice: ")

    if choice == 1:
        admin_menu()

    elif choice == 2:
        customer_menu()

    elif choice == 3:
        print("Thank you for using the Our System, Have a Nice Day")
        break

    else:
        print("Invalid choice, please try again.")