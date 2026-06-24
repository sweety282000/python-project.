#IMPORT : 1> from tkinter import * imports Tkinter GUI classes like Tk, Entry, Button, and Label, so you can use them without writing tkinter. 
# 2>import math loads Python’s math functions such as sin, cos, sqrt, factorial, log, and constants like pi and e, which your calculator later uses while evaluating expressions.

from tkinter import *
import math

#   WINDOW  

root = Tk()           # creates the main application window, which is the base container for all widgets.
root.title("Advanced Scientific Calculator")         # sets the window title bar text
root.geometry("500x565")                             # sets the size
root.resizable(False, False)                         # prevents resizing
root.configure(bg="#f0f0f0")                       # sets the background color of the main window

expression = ""        #is a normal Python string that stores the full math expression the user is typing
equation = StringVar() # creates a Tkinter variable object that is linked to the display box; when you call equation.set(...), the text shown in the Entry widget changes automatically

#   FUNCTIONS  

def press(value):  
    global expression
    expression += str(value)
    equation.set(expression)

def clear():
    global expression
    expression = ""
    equation.set("")

def clear_entry():
    global expression

    if len(expression) > 0:
        expression = expression[:-1]

    equation.set(expression)

def backspace():
    global expression
    expression = expression[:-1]
    equation.set(expression)

def equalpress():
    global expression

    try:
        exp = expression

        exp = exp.replace("asin", "math.asin")
        exp = exp.replace("acos", "math.acos")
        exp = exp.replace("atan", "math.atan")

        exp = exp.replace("sin", "math.sin")
        exp = exp.replace("cos", "math.cos")
        exp = exp.replace("tan", "math.tan")

        exp = exp.replace("log", "math.log10")
        exp = exp.replace("ln", "math.log")

        exp = exp.replace("√", "math.sqrt")

        exp = exp.replace("π", str(math.pi))
        exp = exp.replace("e", str(math.e))

        exp = exp.replace("mod", "%")

        if exp.endswith("!"):
            num = int(exp[:-1])
            result = str(math.factorial(num))
        else:
            result = str(eval(exp))

        equation.set(result)
        expression = result

    except Exception:
        equation.set("Error")
        expression = ""
'''
1> press(value) runs when most buttons are clicked, adds the clicked value to the current expression, and refreshes the display using equation.set(expression).
2> global expression is needed because the function changes the outer variable instead of creating a new local variable
3> clear() removes everything from the calculator by resetting both the internal expression and the visible display to empty text.
4> clear_entry(): Despite the name, this behaves like deleting the last typed character, because expression[:-1] returns the string except for its final character
5> The if len(expression) > 0 check avoids slicing an already empty string unnecessarily.
6> backspace() also removes the last character, so it overlaps with what clear_entry() already does
7> equalpress() is called when = is pressed, and it prepares a temporary version of the typed expression for evaluation.
8> try: is used so that invalid formulas do not crash the program; instead, the calculator can show "Error"
9> " exp = exp.replace("sin", "math.sin") " These lines convert user-friendly button text like sin( into actual Python expressions like math.sin( so eval() can understand them.
10> log is mapped to base-10 log with math.log10, while ln is mapped to natural log with math.log
11>log is mapped to base-10 log with math.log10, while ln is mapped to natural log with math.log
12> √ becomes math.sqrt, so an input like √(25) turns into valid Python math syntax.π and e are replaced with their numeric values from the math module, and mod is converted to %, which is Python’s modulus operator.
13> If the expression ends with !, the code treats it as a factorial and calculates it with math.factorial() after removing the final !.
Otherwise, it uses eval(exp) to evaluate the generated Python expression, which is a common shortcut in simple calculator examples but should be used carefully because eval() executes Python code directly.
14> After a successful calculation, the result is displayed and also saved back into expression, so the answer can be reused for the next operation.
If anything goes wrong, the calculator displays "Error" and clears the stored expression instead of stopping the app.
'''

#   DISPLAY  

entry = Entry(              # This creates the text box where the current expression and result appears
    root,
    textvariable=equation,
    font=("Arial", 24),
    justify="right",
    bg="#cfeee7",
    bd=3,
    relief=SUNKEN
) 
#textvariable=equation links the box to the StringVar, justify="right" aligns text to the right like a real calculator, and the other options control font, border width, color, and sunken visual style

entry.place(   #place() positions the Entry widget at an exact coordinate and size inside the window.
    x=15,
    y=20,
    width=470,
    height=60
)

#   BUTTON DATA  

buttons = [

    ['MC', 'MR', 'M+', 'M-', 'C', '⌫'],

    ['sin', 'cos', 'tan', 'log', 'ln', '/'],

    ['asin', 'acos', 'atan', 'π', 'e', '*'],

    ['7', '8', '9', '√(', '**2', '-'],

    ['4', '5', '6', '**', '!', '+'],

    ['1', '2', '3', 'abs(', '%', '='],

    ['0', '.', '(', ')', 'CE', 'Ans']
]
'''
This is a nested list that defines the calculator buttons row by row, making layout generation easier because the program can loop through the structure instead of creating each button manually.

Some buttons are fully implemented, such as numbers and operators, while others like MC, MR, M+, and M- are only displayed and do not yet have memory logic in your code.
'''


#   BUTTON SETTINGS  

start_x = 15
start_y = 105

btn_width = 68
btn_height = 50

x_gap = 10
y_gap = 10

'''
These variables control where the button grid begins and how large each button is.
x_gap and y_gap define the spacing between buttons, making the layout cleaner and easier to adjust from one place.
'''

#   BUTTON CREATION  

for r in range(len(buttons)):
    for c in range(len(buttons[r])):  # This double loop goes through every row r and every column c inside that row, so each button can be created automatically from the buttons list

        text = buttons[r][c]   #text stores the label for the current button.

        if text == "":
            continue           #If a label were blank, continue would skip creating that button

        if text == "C":
            cmd = clear

        elif text == "⌫":
            cmd = backspace

        elif text == "CE":
            cmd = clear_entry

        elif text == "=":
            cmd = equalpress

        elif text == "Ans":
            cmd = lambda: press(expression)

        elif text in [
            "sin",
            "cos",
            "tan",
            "asin",
            "acos",
            "atan",
            "log",
            "ln",
            "abs"
        ]:
            cmd = lambda t=text: press(t + "(")

        else:
            cmd = lambda t=text: press(t)  

        btn = Button(   #This creates a Tkinter Button widget with the chosen text, font, border style.
            root,
            text=text,
            font=("Arial", 12, "bold"),
            relief=RAISED,
            bd=2,
            command=cmd #tells Tkinter what function to run when the user clicks that button.
        )

        x = start_x + c * (btn_width + x_gap) #positioning of button as per row & col.
        y = start_y + r * (btn_height + y_gap) #As c increases buttons move right; as r increases, buttons move downward.

        btn.place(
            x=x,
            y=y,
            width=btn_width,
            height=btn_height
        )
"""
1> pressing Ans inserts the current result or current expression into the input again by calling press(expression).
2> For function buttons, the code automatically inserts the function name followed by an opening bracket, such as sin( or log(, which is convenient for the user.
3> lambda t=text: ... is important here because in loops, lambda is often used to capture the current button value safely for the button’s callback.
4> cmd = lambda t=text: press(t) All other buttons, like numbers and operators, simply insert their own text into the expression.
"""
#   FOOTER  

footer = Label(
    root,
    text="Made by Sweety",
    font=("Arial", 10, "bold"),
    bg="#f0f0f0",
    fg="black"
)

footer.place(
    x=490,
    y=550,
    anchor="se"
)

#   RUN  

root.mainloop()