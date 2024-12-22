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
    if current and current[-1] not in "+-*/^": 
        display.insert(END, operator)

# Create the main window
window = Tk()
window.title("Enhanced Calculator") 
window.geometry("300x400")  # Set window size
window.configure(bg="#f0f0f0")  # Set background color

# Create the display
display = Entry(window, width=35, borderwidth=5, font=("Arial", 16))
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define buttons with improved styling
button_style = {
    "padx": 40,
    "pady": 20,
    "font": ("Arial", 14),
    "bg": "#e0e0e0",
    "activebackground": "#d0d0d0"
}

button_1 = Button(window, text="1", **button_style, command=lambda: button_click(1))
button_2 = Button(window, text="2", **button_style, command=lambda: button_click(2))
button_3 = Button(window, text="3", **button_style, command=lambda: button_click(3))
button_4 = Button(window, text="4", **button_style, command=lambda: button_click(4))
button_5 = Button(window, text="5", **button_style, command=lambda: button_click(5))
button_6 = Button(window, text="6", **button_style, command=lambda: button_click(6))
button_7 = Button(window, text="7", **button_style, command=lambda: button_click(7))
button_8 = Button(window, text="8", **button_style, command=lambda: button_click(8))
button_9 = Button(window, text="9", **button_style, command=lambda: button_click(9))
button_0 = Button(window, text="0", **button_style, command=lambda: button_click(0))
button_add = Button(window, text="+", **button_style, command=lambda: button_operator("+"))
button_equal = Button(window, text="=", **button_style, command=button_equal, bg="#4CAF50", activebackground="#3e8e41")
button_clear = Button(window, text="Clear", **button_style, command=button_clear, bg="#f44336", activebackground="#d32f2f")

button_subtract = Button(window, text="-", **button_style, command=lambda: button_operator("-"))
button_multiply = Button(window, text="*", **button_style, command=lambda: button_operator("*"))
button_divide = Button(window, text="/", **button_style, command=lambda: button_operator("/"))
button_power = Button(window, text="^", **button_style, command=lambda: button_operator("**"))
button_root = Button(window, text="√", **button_style, command=lambda: button_operator("**(1/2)")) 

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