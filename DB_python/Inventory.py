import mysql.connector

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Atharva",
    database="inventory"
)

# Create a cursor to interact with the database
cursor = db.cursor()

def add_product(name, description, price, quantity):
    sql = "INSERT INTO products (name, description, price, quantity) VALUES (%s, %s, %s, %s)"
    values = (name, description, price, quantity)
    cursor.execute(sql, values)
    db.commit()
    print("Product added successfully!")

def update_product(id, name, description, price, quantity):
    sql = "UPDATE products SET name=%s, description=%s, price=%s, quantity=%s WHERE id=%s"
    values = (name, description, price, quantity, id)
    cursor.execute(sql, values)
    db.commit()
    print("Product updated successfully!")

def delete_product(id):
    sql = "DELETE FROM products WHERE id=%s"
    values = (id,)
    cursor.execute(sql, values)
    db.commit()
    print("Product deleted successfully!")

def view_products():
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    if not products:
        print("No products found.")
    else:
        print("ID\tName\tDescription\tPrice\tQuantity")
        for product in products:
            print(f"{product[0]}\t{product[1]}\t{product[2]}\t{product[3]}\t{product[4]}")

while True:
    print("\nInventory Management System")
    print("1. Add Product")
    print("2. Update Product")
    print("3. Delete Product")
    print("4. View Products")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter product name: ")
        description = input("Enter product description: ")
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))
        add_product(name, description, price, quantity)

    elif choice == "2":
        id = int(input("Enter product ID to update: "))
        name = input("Enter new product name: ")
        description = input("Enter new product description: ")
        price = float(input("Enter new product price: "))
        quantity = int(input("Enter new product quantity: "))
        update_product(id, name, description, price, quantity)

    elif choice == "3":
        id = int(input("Enter product ID to delete: "))
        delete_product(id)

    elif choice == "4":
        view_products()

    elif choice == "5":
        break

    else:
        print("Invalid choice. Please try again.")

# Close the database connection
db.close()