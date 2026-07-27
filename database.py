import mysql.connector
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

# Connect to MySQL Server
mydb = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    passwd=DB_PASSWORD
)

mycursor = mydb.cursor()


def setup_database():
    """Creates the database and required tables if they don't exist."""

    mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    mycursor.execute(f"USE {DB_NAME}")

    # Login Table
    mycursor.execute("""
        CREATE TABLE IF NOT EXISTS login(
            username VARCHAR(25) NOT NULL,
            password VARCHAR(25) NOT NULL
        )
    """)

    # Purchase Table
    mycursor.execute("""
        CREATE TABLE IF NOT EXISTS purchase(
            odate DATE NOT NULL,
            name VARCHAR(25) NOT NULL,
            mobile VARCHAR(15) NOT NULL,
            pcode INT NOT NULL,
            qty INT NOT NULL,
            price INT NOT NULL
        )
    """)

    # Stock Table
    mycursor.execute("""
        CREATE TABLE IF NOT EXISTS stock(
            pcode INT NOT NULL,
            pname VARCHAR(25) NOT NULL,
            quantity INT NOT NULL,
            price INT NOT NULL
        )
    """)

    mydb.commit()

    # Insert default admin account only if table is empty
    mycursor.execute("SELECT * FROM login")

    if len(mycursor.fetchall()) == 0:
        mycursor.execute(
            "INSERT INTO login VALUES (%s, %s)",
            ("username", "password")
        )
        mydb.commit()