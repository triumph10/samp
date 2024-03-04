import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

class VirtualTourApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Virtual Tour")

        # Create a 3D plot
        self.fig = plt.Figure(figsize=(8, 6))
        self.ax = self.fig.add_subplot(111, projection='3d')

        # Generate some sample 3D data (replace with your own)
        x = np.linspace(0, 5, 100)
        y = np.linspace(-5, 5, 100)
        X, Y = np.meshgrid(x, y)
        Z = np.sin(np.sqrt(X**2 + Y**2))

        self.ax.plot_surface(X, Y, Z, cmap='viridis')

        # Create Matplotlib canvas
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = VirtualTourApp(root)
    root.mainloop()
