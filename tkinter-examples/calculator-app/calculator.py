import tkinter
import parser

root = tkinter.Tk()
root.title("Calculator")

# get the user input and place it in the text feild
i = 0


def get_variables(num):
    global i
    display.insert(i, num)
    i += 1


def calculate():
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "ERROR")


def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length


def clear_all():
    display.delete(0, "end")


def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all()
        display.insert(0, "ERROR")


# adding the input feild
display = tkinter.Entry(root)
display.grid(row=1, columnspan=6, sticky="w"+"e")

# adding buttons to the Calculator
tkinter.Button(root, text="1", command=lambda: get_variables(1)).grid(row=2, column=0)
tkinter.Button(root, text="2", command=lambda: get_variables(2)).grid(row=2, column=1)

tkinter.Button(root, text="3", command=lambda: get_variables(3)).grid(row=2, column=2)

tkinter.Button(root, text="4", command=lambda: get_variables(4)).grid(row=3, column=0)
tkinter.Button(root, text="5", command=lambda: get_variables(5)).grid(row=3, column=1)
tkinter.Button(root, text="6", command=lambda: get_variables(6)).grid(row=3, column=2)

tkinter.Button(root, text="7", command=lambda: get_variables(7)).grid(row=4, column=0)
tkinter.Button(root, text="8", command=lambda: get_variables(8)).grid(row=4, column=1)
tkinter.Button(root, text="9", command=lambda: get_variables(9)).grid(row=4, column=2)

# adding other buttons to the Calculator
tkinter.Button(root, text="AC", command=lambda: clear_all()).grid(row=5, column=0)
tkinter.Button(root, text="0", command=lambda: get_variables(0)).grid(row=5, column=1)
tkinter.Button(root, text="=", command=lambda: calculate()).grid(row=5, column=2)

tkinter.Button(root, text="+", command=lambda: get_operation("+")).grid(row=2, column=3)
tkinter.Button(root, text="-", command=lambda: get_operation("-")).grid(row=3, column=3)
tkinter.Button(root, text="*", command=lambda: get_operation("*")).grid(row=4, column=3)
tkinter.Button(root, text="/", command=lambda: get_operation("/")).grid(row=5, column=3)

# adding new operation buttons to the Calculator
tkinter.Button(root, text="pi", command=lambda: get_operation("*3.14")).grid(row=2, column=4)
tkinter.Button(root, text="%", command=lambda: get_operation("%")).grid(row=3, column=4)
tkinter.Button(root, text="(", command=lambda: get_operation("(")).grid(row=4, column=4)
tkinter.Button(root, text="exp", command=lambda: get_operation("--")).grid(row=5, column=4)

tkinter.Button(root, text="<-", command=lambda: undo()).grid(row=2, column=5)
tkinter.Button(root, text="x!").grid(row=3, column=5)
tkinter.Button(root, text=")", command=lambda: get_operation(")")).grid(row=4, column=5)
tkinter.Button(root, text="^2", command=lambda: get_operation("**")).grid(row=5, column=5)


root.mainloop()
