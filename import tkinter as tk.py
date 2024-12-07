import tkinter as tk
from tkinter import messagebox

def on_button_click():
    messagebox.showinfo("Hello", "you suck man!")
  

# Set up the main application window
app = tk.Tk()
app.title("TT's first app")
app.geometry("314x215")  # width x height

# Create a label
label = tk.Label(app, text="Hello, User! Click the button below.")
label.pack(pady=10)

# Create a button
button = tk.Button(app, text="Click Me!", command=on_button_click)
button.pack(pady=10)

# Start the main application loop
app.mainloop()
