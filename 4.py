import tkinter as tk
from tkinter import ttk

def sell_property():
    property_type = property_type_var.get()
    property_subtype = property_subtype_var.get()
    phone_number = phone_entry.get()

    # Add more fields and logic as needed (e.g., image handling, database integration)

    print(f"Property Type: {property_type}")
    print(f"Property Subtype: {property_subtype}")
    print(f"Phone Number: {phone_number}")

root = tk.Tk()
root.title("Real Estate Selling")

# Property Type (Residential/Commercial)
property_type_var = tk.StringVar()
property_type_var.set("Residential")  # Default value
property_type_label = tk.Label(root, text="Property Type:")
property_type_label.pack()
property_type_menu = ttk.Combobox(root, textvariable=property_type_var, values=["Residential", "Commercial"])
property_type_menu.pack()

# Property Subtype (Flat/Apartment, Independent House/Villa, etc.)
property_subtype_var = tk.StringVar()
property_subtype_label = tk.Label(root, text="Property Subtype:")
property_subtype_label.pack()
property_subtype_entry = tk.Entry(root, textvariable=property_subtype_var)
property_subtype_entry.pack()

# Phone Number
phone_label = tk.Label(root, text="Phone Number:")
phone_label.pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

# Sell Button
sell_button = tk.Button(root, text="Sell Property", command=sell_property)
sell_button.pack()

root.mainloop()
