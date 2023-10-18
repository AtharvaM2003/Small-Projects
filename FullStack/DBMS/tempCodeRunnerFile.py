import tkinter as tk
import mysql.connector

# Database connection parameters
db_config = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "Atharva",
    "database": "my_database"
}

# Create a function to register a user and store data in the database
def register():
    name = name_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    insert_query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
    data = (name, email, password)

    try:
        cursor.execute(insert_query, data)
        conn.commit()
        result_label.config(text=f"Registration successful for {name}!")
    except mysql.connector.Error as err:
        conn.rollback()
        result_label.config(text=f"Error: {err}")
    finally:
        cursor.close()
        conn.close()

# Create a function to delete a user
def delete():
    email = email_entry.get()

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    delete_query = "DELETE FROM users WHERE email = %s"
    data = (email,)

    try:
        cursor.execute(delete_query, data)
        conn.commit()
        result_label.config(text=f"User with email {email} deleted.")
    except mysql.connector.Error as err:
        conn.rollback()
        result_label.config(text=f"Error: {err}")
    finally:
        cursor.close()
        conn.close()

# Create a function to edit a user's password
def edit():
    email = email_entry.get()
    new_password = new_password_entry.get()

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    update_query = "UPDATE users SET password = %s WHERE email = %s"
    data = (new_password, email)

    try:
        cursor.execute(update_query, data)
        conn.commit()
        result_label.config(text=f"Password updated for user with email {email}.")
    except mysql.connector.Error as err:
        conn.rollback()
        result_label.config(text=f"Error: {err}")
    finally:
        cursor.close()
        conn.close()

# Create the main application window
app = tk.Tk()
app.title("User Management Form")

# Set the window size
app.geometry("400x300")  # Width x Height

# Create and arrange labels and entry widgets using the grid layout
name_label = tk.Label(app, text="Name:")
name_entry = tk.Entry(app)
email_label = tk.Label(app, text="Email:")
email_entry = tk.Entry(app)
password_label = tk.Label(app, text="Password:")
password_entry = tk.Entry(app, show="*")
new_password_label = tk.Label(app, text="New Password (for editing):")
new_password_entry = tk.Entry(app, show="*")

name_label.grid(row=0, column=0, sticky="w")
name_entry.grid(row=0, column=1)
email_label.grid(row=1, column=0, sticky="w")
email_entry.grid(row=1, column=1)
password_label.grid(row=2, column=0, sticky="w")
password_entry.grid(row=2, column=1)
new_password_label.grid(row=3, column=0, sticky="w")
new_password_entry.grid(row=3, column=1)

register_button = tk.Button(app, text="Register", command=register)
delete_button = tk.Button(app, text="Delete", command=delete)
edit_button = tk.Button(app, text="Edit Password", command=edit)
result_label = tk.Label(app, text="")

register_button.grid(row=4, column=0, columnspan=2)
delete_button.grid(row=5, column=0, columnspan=2)
edit_button.grid(row=6, column=0, columnspan=2)
result_label.grid(row=7, column=0, columnspan=2)

# Run the application
app.mainloop()
