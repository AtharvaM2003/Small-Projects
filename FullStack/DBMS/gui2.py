import tkinter as tk
from tkinter import messagebox
from pymongo import MongoClient

def register():
    username = entry_username.get()
    password = entry_password.get()
    confirm_password = entry_confirm_password.get()
    name = entry_name.get()
    email = entry_email.get()

    if not username or not password or not confirm_password or not name or not email:
        messagebox.showerror("Error", "Please fill in all fields.")
    elif password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match.")
    else:
        # MongoDB connectivity
        client = MongoClient("mongodb://localhost:27017")
        db = client["simple"]
        collection = db["rege"]

        # Check if the username or email already exists
        if collection.find_one({"$or": [{"username": username}, {"email": email}]}):
            messagebox.showerror("Error", "Username or email already exists.")
        else:
            # Insert the registration data into MongoDB
            user_data = {
                "username": username,
                "password": password,
                "name": name,
                "email": email
            }
            collection.insert_one(user_data)
            messagebox.showinfo("Success", f"Registration successful for user: {username}")
        client.close()

def update():
    username = entry_username.get()
    name = entry_name.get()
    email = entry_email.get()

    # MongoDB connectivity
    client = MongoClient("mongodb://localhost:27017")
    db = client["simple"]
    collection = db["rege"]

    # Check if the username or email already exists
    existing_user = collection.find_one({"$or": [{"username": username}, {"email": email}]})
    if existing_user:
        # Update user details
        collection.update_one(
            {"_id": existing_user["_id"]},
            {"$set": {"name": name, "email": email}}
        )
        messagebox.showinfo("Success", f"User details updated for user: {username}")
    else:
        messagebox.showerror("Error", "User not found.")
    client.close()

def delete():
    username = entry_username.get()

    # MongoDB connectivity
    client = MongoClient("mongodb://localhost:27017")
    db = client["simple"]
    collection = db["rege"]

    # Check if the username exists and delete the user
    existing_user = collection.find_one({"username": username})
    if existing_user:
        collection.delete_one({"_id": existing_user["_id"]})
        messagebox.showinfo("Success", f"User {username} deleted.")
    else:
        messagebox.showerror("Error", "User not found.")
    client.close()

# Create the main window
root = tk.Tk()
root.title("Registration Form")

# Increase the frame size
frame_width = 400
frame_height = 300
root.geometry(f"{frame_width}x{frame_height}")

# Create labels and entry fields with increased line spacing
label_name = tk.Label(root, text="Name:")
label_email = tk.Label(root, text="Email:")
label_username = tk.Label(root, text="Username:")
label_password = tk.Label(root, text="Password:")
label_confirm_password = tk.Label(root, text="Confirm Password:")

entry_name = tk.Entry(root)
entry_email = tk.Entry(root)
entry_username = tk.Entry(root)
entry_password = tk.Entry(root, show="*")  # Mask the password
entry_confirm_password = tk.Entry(root, show="*")

# Create registration, update, and delete buttons
register_button = tk.Button(root, text="Register", command=register)
update_button = tk.Button(root, text="Update", command=update)
delete_button = tk.Button(root, text="Delete", command=delete)

# Layout using the grid geometry manager with increased line spacing
label_name.grid(row=0, column=0, sticky="w", padx=10, pady=5)
label_email.grid(row=1, column=0, sticky="w", padx=10, pady=5)
label_username.grid(row=2, column=0, sticky="w", padx=10, pady=5)
label_password.grid(row=3, column=0, sticky="w", padx=10, pady=5)
label_confirm_password.grid(row=4, column=0, sticky="w", padx=10, pady=5)

entry_name.grid(row=0, column=1, padx=10, pady=5)
entry_email.grid(row=1, column=1, padx=10, pady=5)
entry_username.grid(row=2, column=1, padx=10, pady=5)
entry_password.grid(row=3, column=1, padx=10, pady=5)
entry_confirm_password.grid(row=4, column=1, padx=10, pady=5)

register_button.grid(row=5, column=0, padx=10, pady=10)
update_button.grid(row=5, column=1, padx=10, pady=10)
delete_button.grid(row=5, column=2, padx=10, pady=10)

# Start the main loop
root.mainloop()
