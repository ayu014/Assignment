import tkinter as tk
from tkinter import messagebox
import math

# Function to perform calculations
def calculate():
    try:
        first = float(entry_first.get())
        operation = operation_var.get()
        
        if operation in ['+', '-', '*', '/']:
            second = float(entry_second.get())
            if operation == '+':
                result = first + second
            elif operation == '-':
                result = first - second
            elif operation == '*':
                result = first * second
            elif operation == '/':
                if second == 0:
                    raise ValueError("Cannot divide by zero.")
                result = first / second
        elif operation == '^':
            second = float(entry_second.get())
            result = first ** second
        elif operation == '√':
            result = math.sqrt(first)
        else:
            raise ValueError("Invalid operation selected.")
        
        label_result.config(text=f"Result: {result}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x300")
root.configure(bg="#f0f0f0")

# Create UI elements
label_first = tk.Label(root, text="First Number:", bg="#f0f0f0")
label_first.pack(pady=5)

entry_first = tk.Entry(root)
entry_first.pack(pady=5)

label_second = tk.Label(root, text="Second Number (if needed):", bg="#f0f0f0")
label_second.pack(pady=5)

entry_second = tk.Entry(root)
entry_second.pack(pady=5)

operation_var = tk.StringVar(value='+')
operations = ['+', '-', '*', '/', '^', '√']
for operation in operations:
    radio = tk.Radiobutton(root, text=operation, variable=operation_var, value=operation, bg="#f0f0f0")
    radio.pack(anchor=tk.W)

button_calculate = tk.Button(root, text="Calculate", command=calculate, bg="#4CAF50", fg="white")
button_calculate.pack(pady=20)

label_result = tk.Label(root, text="Result: ", bg="#f0f0f0")
label_result.pack(pady=5)

# Start the GUI event loop
root.mainloop()