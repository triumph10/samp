import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class PanoramicViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("360-Degree Image Viewer")

        # Create an empty canvas for the image
        self.canvas = tk.Canvas(root, width=800, height=400)
        self.canvas.pack()

        # Load a sample 360-degree image (replace with your own)
        self.image_path = r"C:\Users\Siddhesh Patil\Downloads\WhatsApp Image 2024-02-29 at 18.06.33.jpeg"
        self.load_image()

        # Bind mouse events for panning the image
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_move)

    def load_image(self):
        img = Image.open(self.image_path)
        img = img.resize((800, 400), Image.LANCZOS)  # Use LANCZOS resampling
        self.photo = ImageTk.PhotoImage(img)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo, tags="image")
        self.image_width = img.width
        self.image_height = img.height

    def on_button_press(self, event):
        # Record the starting position of the mouse
        self.start_x = event.x

    def on_move(self, event):
        # Calculate the distance moved by the mouse
        delta_x = event.x - self.start_x
        # Calculate the amount of rotation based on mouse movement
        rotation = delta_x / 10  # Adjust the division factor for sensitivity
        # Adjust the image position based on the rotation
        self.canvas.delete("image")
        img = Image.open(self.image_path)
        img = img.resize((800, 400), Image.LANCZOS)  # Use LANCZOS resampling
        img = img.rotate(rotation)  # Rotate the image
        self.photo = ImageTk.PhotoImage(img)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo, tags="image")
        self.start_x = event.x

if __name__ == "__main__":
    root = tk.Tk()
    app = PanoramicViewer(root)
    root.mainloop()
