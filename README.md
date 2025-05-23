Skills Demonstrated
Python OOP: classes, methods, attributes

Error handling with exceptions

Composition (object within an object)

Simple text-based UI

Git & GitHub for version control

Writing clean and modular code

bestbuy/
│
├── products.py     # Product class definition
├── store.py        # Store class definition
├── main.py         # Program entry point + user interface


# 🛍️ BestBuy Store Project – Python OOP  
### Created by Lukas

---

## 🎯 Project Goal

The goal of this project was to build a simple but realistic simulation of a store using Python. The system lets users:

- View and manage products
- Track product quantity and status
- Place multi-item orders through a user-friendly terminal interface

The project was developed in **PyCharm**, using **Git** and **GitHub** for version control.

---

## 🔧 Step-by-Step Development

---

### 🧩 Step 1 – `Product` Class

Defined in `products.py`, this class models each item in the store.

#### Key Attributes:
- `name`: Product name (e.g. MacBook)
- `price`: Price per unit
- `quantity`: Items in stock
- `active`: If the product is available for sale

#### Key Methods:
- `buy(quantity)`: Decreases stock, returns total cost
- `set_quantity(quantity)`: Updates stock, disables if 0
- `activate()` / `deactivate()`
- `is_active()`
- `show()`: Displays product info

This step taught me how to structure a Python class and handle validation with exceptions.

---

### 🏬 Step 2 – `Store` Class

Defined in `store.py`, this class manages multiple `Product` objects.

#### Key Methods:
- `add_product(product)`
- `remove_product(product)`
- `get_total_quantity()`: Sum of all product quantities
- `get_all_products()`: Returns only active products
- `order(shopping_list)`: Processes a list of (Product, quantity) pairs

This demonstrated composition (a store *has* products), list management, and OOP principles.

---

### 💻 Step 3 – User Interface

The interface was written in `main.py` and uses a loop to show a menu:


- Lets users buy products by number and quantity
- Shows real-time updates to stock
- Handles errors like invalid input or out-of-stock orders

This part brought all the components together into a functioning program.

---

## 🌐 Version Control with Git & GitHub

- Used `git init`, `git add`, `git commit`, and `git push` to track changes
- Pushed the code to a **public GitHub repository**:


git remote add origin https://github.com/USERNAME/bestbuy.git
git branch -M main
git push -u origin main


This gave me real-world experience with repositories and commit history.

---

## 🧠 Skills Gained

- Python OOP (classes, attributes, methods)
- Error handling with `try`, `except`
- Composition in class design
- Interactive command-line programming
- Git & GitHub for code management

---



