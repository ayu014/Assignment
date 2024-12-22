from tkinter import *

def button_click(number):
    current = display.get()
    display.delete(0, END)
    display.insert(0, str(current) + str(number))

def button_clear():
    display.delete(0, END)

def button_equal():
    try:
        result = eval(display.get())
        display.delete(0, END)
        display.insert(0, str(result))
    except:
        display.delete(0, END)
        display.insert(0, "Error")

def button_operator(operator):
    current = display.get()
    if current and current[-1] not in "+-*/^":  # Prevent consecutive operators
        display.insert(END, operator)

# Create the main window
window = Tk()
window.title("Enhanced Calculator") 
window.geometry("300x400")  # Set window size
window.configure(bg="#f0f0f0")  # Set background color

# Create the display
display = Entry(window, width=35, borderwidth=5, font=("Arial", 16))
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define button styles
button_style = {
    "padx": 40,
    "pady": 20,
    "font": ("Arial", 14),
    "bg": "#e0e0e0",
    "activebackground": "#d0d0d0"
}

# Function to create buttons with consistent styling
def create_button(text, command):
    button_config = button_style.copy()  # Create a copy to avoid modifying the original
    if text == "Clear":
        button_config["bg"] = "#f44336"
        button_config["activebackground"] = "#d32f2f"
    return Button(window, text=text, **button_config, command=command)

# Create buttons using the create_button function
button_1 = create_button("1", lambda: button_click(1))
button_2 = create_button("2", lambda: button_click(2))
button_3 = create_button("3", lambda: button_click(3))
button_4 = create_button("4", lambda: button_click(4))
button_5 = create_button("5", lambda: button_click(5))
button_6 = create_button("6", lambda: button_click(6))
button_7 = create_button("7", lambda: button_click(7))
button_8 = create_button("8", lambda: button_click(8))
button_9 = create_button("9", lambda: button_click(9))
button_0 = create_button("0", lambda: button_click(0))
button_add = create_button("+", lambda: button_operator("+"))
button_equal = create_button("=", lambda: button_equal())
button_clear = create_button("Clear", button_clear) 
button_subtract = create_button("-", lambda: button_operator("-"))
button_multiply = create_button("*", lambda: button_operator("*"))
button_divide = create_button("/", lambda: button_operator("/"))
button_power = create_button("^", lambda: button_operator("**"))
button_root = create_button("√", lambda: button_operator("**(1/2)")) 

# Place buttons on the grid
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=1, column=3)
button_equal.grid(row=4, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=2)
button_power.grid(row=2, column=4)
button_root.grid(row=3, column=4)

# Start the GUI event loop
window.mainloop()