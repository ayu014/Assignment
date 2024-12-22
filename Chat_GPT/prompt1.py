import tkinter as tk
from tkinter import messagebox
import math

def add(first, second):
    return first + second

def minus(first, second):
    return first - second

def multi(first, second):
    return first * second

def divide(first, second):
    try:
        return first / second
    except ZeroDivisionError:
        messagebox.showerror("Error", "Division by zero is not allowed!")
        return None

def expo(first, second):
    return first ** second

def root(number):
    if number < 0:
        messagebox.showerror("Error", "Cannot calculate the square root of a negative number!")
        return None
    return math.sqrt(number)

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        # Entry widget to display numbers and results
        self.entry = tk.Entry(root, width=30, borderwidth=5, font=("Arial", 16))
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Buttons
        self.create_buttons()

        # Variables to store calculations
        self.first_number = None
        self.operation = None

    def create_buttons(self):
        button_texts = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("C", 4, 0), ("0", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("^", 5, 0), ("√", 5, 1)
        ]

        for text, row, col in button_texts:
            if text == "=":
                button = tk.Button(self.root, text=text, width=10, height=2, command=self.calculate)
            elif text == "C":
                button = tk.Button(self.root, text=text, width=10, height=2, command=self.clear)
            elif text == "√":
                button = tk.Button(self.root, text=text, width=10, height=2, command=lambda: self.perform_operation("√"))
            else:
                button = tk.Button(self.root, text=text, width=10, height=2, command=lambda t=text: self.button_click(t))

            button.grid(row=row, column=col, padx=5, pady=5)

    def button_click(self, value):
        if value in "+-*/^":
            self.first_number = float(self.entry.get())
            self.operation = value
            self.entry.delete(0, tk.END)
        else:
            current = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(0, current + value)

    def calculate(self):
        if self.first_number is not None and self.operation is not None:
            second_number = float(self.entry.get())
            result = None

            if self.operation == "+":
                result = add(self.first_number, second_number)
            elif self.operation == "-":
                result = minus(self.first_number, second_number)
            elif self.operation == "*":
                result = multi(self.first_number, second_number)
            elif self.operation == "/":
                result = divide(self.first_number, second_number)
            elif self.operation == "^":
                result = expo(self.first_number, second_number)

            if result is not None:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(result))

            self.first_number = None
            self.operation = None

    def perform_operation(self, op):
        if op == "√":
            number = float(self.entry.get())
            result = root(number)
            if result is not None:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(result))

    def clear(self):
        self.entry.delete(0, tk.END)

# Create the main application window
root = tk.Tk()
app = CalculatorApp(root)
root.mainloop()
