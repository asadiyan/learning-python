import tkinter
import parser

root = tkinter.Tk()
root.title("Calculator")

# adding the input feild
display = tkinter.Entry(root)
display.grid(row=1, columnspan=6, sticky="w"+"e")

# adding buttons to the Calculator
tkinter.Button(root, text="1").grid(row=2, column=0)
tkinter.Button(root, text="2").grid(row=2, column=1)
tkinter.Button(root, text="3").grid(row=2, column=2)

tkinter.Button(root, text="4").grid(row=3, column=0)
tkinter.Button(root, text="5").grid(row=3, column=1)
tkinter.Button(root, text="6").grid(row=3, column=2)

tkinter.Button(root, text="7").grid(row=4, column=0)
tkinter.Button(root, text="8").grid(row=4, column=1)
tkinter.Button(root, text="9").grid(row=4, column=2)

# adding other buttons to the Calculator
tkinter.Button(root, text="AC").grid(row=5, column=0)
tkinter.Button(root, text="0").grid(row=5, column=1)
tkinter.Button(root, text="=").grid(row=5, column=2)

tkinter.Button(root, text="+").grid(row=2, column=3)
tkinter.Button(root, text="-").grid(row=3, column=3)
tkinter.Button(root, text="*").grid(row=4, column=3)
tkinter.Button(root, text="/").grid(row=5, column=3)

# adding new operation buttons to the Calculator
tkinter.Button(root, text="pi").grid(row=2, column=4)
tkinter.Button(root, text="%").grid(row=3, column=4)
tkinter.Button(root, text="(").grid(row=4, column=4)
tkinter.Button(root, text="exp").grid(row=5, column=4)

tkinter.Button(root, text="<-").grid(row=2, column=5)
tkinter.Button(root, text="x!").grid(row=3, column=5)
tkinter.Button(root, text=")").grid(row=4, column=5)
tkinter.Button(root, text="^2").grid(row=5, column=5)


root.mainloop()
