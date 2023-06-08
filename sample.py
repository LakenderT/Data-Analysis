import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import pandas as pd

# Create a sample dataset
data = {
    'Month': ['January', 'February', 'March', 'April', 'May'],
    'Revenue': [5000, 7000, 5500, 6000, 8000],
    'Expenses': [4000, 4500, 5000, 5500, 6000]
}

df = pd.DataFrame(data)

# Function to plot a bar graph
def plot_graph():
    plt.bar(df['Month'], df['Revenue'], label='Revenue')
    plt.bar(df['Month'], df['Expenses'], label='Expenses')
    plt.xlabel('Month')
    plt.ylabel('Amount')
    plt.title('Revenue vs Expenses')
    plt.legend()
    plt.show()

# Create the main window
root = tk.Tk()
root.title('Data Analysis Dashboard')

# Create heading label
heading_label = ttk.Label(root, text='Data Analysis Dashboard', font=('Arial', 18, 'bold'))
heading_label.pack(pady=10)

# Create a notebook widget
notebook = ttk.Notebook(root)
notebook.pack(pady=10)

# Create a frame for the graph
graph_frame = ttk.Frame(notebook)
graph_frame.pack()

# Add the graph frame to the notebook
notebook.add(graph_frame, text='Graph')

# Add a button to plot the graph
plot_button = ttk.Button(graph_frame, text='Plot Graph', command=plot_graph)
plot_button.pack(pady=10)

# Create footer label
footer_label = ttk.Label(root, text='Made by Lakender Tyagi', font=('Arial', 10))
footer_label.pack(pady=5)

# Start the main loop
root.mainloop()
