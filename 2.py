import tkinter as tk
from tkinter import *
from tkinter import filedialog  # For image selection
import os

def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.jpeg")])
    if file_path:
        # Process the selected image (e.g., save it, display it, etc.)
        print(f"Selected image: {file_path}")

def sell_property():
    # Retrieve information from input fields
    selling_price = entry_price.get()
    locality = entry_locality.get()
    sqft_area = entry_sqft.get()
    # Add more fields as needed

    # Perform additional logic (e.g., save data to a database, display confirmation, etc.)
    print(f"Selling Price: {selling_price}")
    print(f"Locality: {locality}")
    print(f"Square Footage: {sqft_area}")
    # Add more logic here

root = Tk()
root.title("Real Estate Selling")

# Create input fields
Label(root, text="Selling Price:").pack()
entry_price = Entry(root)
entry_price.pack()

Label(root, text="Locality:").pack()
entry_locality = Entry(root)
entry_locality.pack()

Label(root, text="Square Footage:").pack()
entry_sqft = Entry(root)
entry_sqft.pack()

# Add more input fields (e.g., image selection, services, etc.)

# Button to select an image
Button(root, text="Select Image", command=select_image).pack()

# Button to sell the property
Button(root, text="Sell Property", command=sell_property).pack()

root.mainloop()
