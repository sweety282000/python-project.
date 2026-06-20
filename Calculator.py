from tkinter import *

# ---------------- WINDOW ----------------
root = Tk()
root.title("Simple Calculator")
root.geometry("320x430")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

expression = ""
equation = StringVar()

# ---------------- FUNCTIONS ----------------
def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def equalpress():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

# ---------------- DISPLAY ----------------
entry = Entry(
    root,
    textvariable=equation,
    font=("Arial", 24),
    justify="right",
    bg="#cfeee7",
    bd=3,
    relief=SUNKEN
)

entry.place(
    x=18,
    y=20,
    width=280,
    height=45
)

# ---------------- BUTTON DATA ----------------
buttons = [
    ['C', '(', ')', '/'],
    ['7', '8', '9', '*'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['.', '0', '%', '=']
]

# ---------------- BUTTONS ----------------
start_x = 18
start_y = 90

btn_width = 55
btn_height = 45

x_gap = 15
y_gap = 15

for r in range(len(buttons)):
    for c in range(len(buttons[r])):

        text = buttons[r][c]

        if text == "C":
            cmd = clear
        elif text == "=":
            cmd = equalpress
        else:
            cmd = lambda t=text: press(t)

        btn = Button(
            root,
            text=text,
            font=("Arial", 16),
            relief=RAISED,
            bd=2,
            command=cmd
        )

        x = start_x + c * (btn_width + x_gap)
        y = start_y + r * (btn_height + y_gap)

        btn.place(
            x=x,
            y=y,
            width=btn_width,
            height=btn_height
        )

root.mainloop()