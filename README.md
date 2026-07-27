# Retail Shop Management System

A console-based **Retail Shop Management System** built using **Python** and **MySQL**. This application provides separate interfaces for **Admin** and **Customer**, allowing inventory management, shopping cart functionality, purchase history, and sales analytics.



## Features:

### Admin

- Secure password-protected login
- Add new products
- Update product prices
- Restock existing products
- Delete products
- Display complete inventory
- Search products by code or name
- View customer purchase history
- Change admin password
- Dashboard
- Reports & Analytics

### Customer

- View all available products
- Search products by name 
- View Shopping Cart
- Add items to cart
- Remove items from cart
- Checkout & Payment
- Purchase History



# Dashboard

The Admin Dashboard displays:

- Total Products
- Total Inventory Value
- Low Stock Items
- Out of Stock Items
- Total Revenue
- Total Orders


# Reports & Analytics

The project includes the following reports:

- Revenue Report
- Inventory Value Report
- Best Selling Product
- Least Selling Product
- Low Stock Report
- Out of Stock Report


# Shopping Cart

The shopping cart system includes:

- Add products
- Quantity reservation
- Stock validation
- Remove items from cart
- Automatic total calculation
- Secure checkout
- Automatic stock deduction after purchase


# Inventory Management

Inventory features include:

- Product Code
- Product Name
- Quantity
- Price
- Low Stock Detection
- Out of Stock Detection


# Database Structure

The project uses **MySQL** with three tables.


## login

| Column   |   Type      |
|----------|-------------|
| username | VARCHAR(25) |
| password | VARCHAR(25) |


## stock

| Column   |  Type       |
|----------|-------------|
| pcode    | INT         |
| pname    | VARCHAR(25) |
| quantity | INT         |
| price    | INT         |


## purchase

| Column | Type        |
|--------|-------------|
| odate  | DATE        |
| name   | VARCHAR(25) |
| mobile | VARCHAR(15) |
| pcode  | INT         |
| qty    | INT         |
| price  | INT         |


# Project Structure

Retail-Shop-Management
│
├── main.py
├── config.py
├── database.py
├── utils.py
├── cart.py
├── reports.py
├── history.py
├── admin.py
├── customer.py
│
├── requirements.txt
├── README.md
└── .gitignore

# Technologies Used

- Python 3
- MySQL
- mysql-connector-python


# Installation

## 1. Clone the repository

git clone https://github.com/yourusername/Retail-Shop-Management.git

## 2. Open the project

cd Retail-Shop-Management

## 3. Install dependencies

pip install -r requirements.txt

## 4. Configure MySQL

Open **config.py**

DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "your_password"
DB_NAME = "shop"


## 5. Run the application

python main.py

The program will automatically create:

- Database
- Required Tables
- Default Admin Account


# 🔐 Default Admin Login

Username - username

Password - password


> It is recommended to change the password after the first login.


# 🚀 Future Improvements

- Graphical User Interface (Tkinter / PyQt)
- Employee Management
- Sales Graphs
- Export Reports to PDF
- Export Reports to Excel
- Product Categories
- GST Billing
- Receipt Generation


# 📖 Learning Outcomes

This project demonstrates practical implementation of:

- Python Programming
- Modular Programming
- Object-Oriented Design Principles
- MySQL Database Management
- CRUD Operations
- Input Validation
- Data Persistence
- SQL Queries
- Inventory Management
- Sales Analytics
- Console Application Development


# 👨‍💻 Author

**Vibhav Singh Rawat**

Developed as a personal academic project to strengthen Python programming, MySQL database management, and software engineering skills.


# 📜 License

This project is licensed under the MIT License.

Feel free to use, modify, and improve the project for learning purposes.