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

def square_root(number):  # Renamed from 'root' to 'square_root'
    if number < 0:
        messagebox.showerror("Error", "Cannot calculate the square root of a negative number!")
        return None
    return math.sqrt(number)


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Enhanced Calculator")
        self.root.geometry("350x400")
        self.root.configure(bg="#f0f0f0")

        # Entry widget to display numbers and results
        self.entry = tk.Entry(root, width=20, borderwidth=2, font=("Arial", 24), justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        self.entry.bind("<Key>", self.key_input)

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
                button = tk.Button(self.root, text=text, width=5, height=2, bg="#4caf50", fg="white", font=("Arial", 14), command=self.calculate)
            elif text == "C":
                button = tk.Button(self.root, text=text, width=5, height=2, bg="#f44336", fg="white", font=("Arial", 14), command=self.clear)
            elif text == "√":
                button = tk.Button(self.root, text=text, width=5, height=2, bg="#2196f3", fg="white", font=("Arial", 14), command=lambda: self.perform_operation("√"))
            else:
                button = tk.Button(self.root, text=text, width=5, height=2, bg="#e0e0e0", font=("Arial", 14), command=lambda t=text: self.button_click(t))

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
            try:
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
            except ValueError:
                messagebox.showerror("Error", "Invalid input!")

    def perform_operation(self, op):
        try:
            if op == "√":
                number = float(self.entry.get())
                result = square_root(number)  # Use the renamed function
                if result is not None:
                    self.entry.delete(0, tk.END)
                    self.entry.insert(0, str(result))
        except ValueError:
            messagebox.showerror("Error", "Invalid input for square root!")


    def clear(self):
        self.entry.delete(0, tk.END)

    def key_input(self, event):
        key = event.char
        keycode = event.keycode

        # Map numpad keys to their respective characters
        numpad_keys = {
            96: "0", 97: "1", 98: "2", 99: "3", 100: "4",
            101: "5", 102: "6", 103: "7", 104: "8", 105: "9",
            110: ".", 107: "+", 109: "-", 106: "*", 111: "/"
        }

        if key.isdigit() or key == ".":
            current = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(0, current + key)
        elif key in "+-*/^":
            self.button_click(key)
        elif key == "\r":  # Enter key
            self.calculate()
        elif key == "\x08":  # Backspace key
            current = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(0, current[:-1])
        elif keycode in numpad_keys:
            self.button_click(numpad_keys[keycode])

# Create the main application window
root = tk.Tk()
app = CalculatorApp(root)
root.mainloop()
