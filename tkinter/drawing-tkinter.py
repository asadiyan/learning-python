import tkinter

root = tkinter.Tk()

canvas = tkinter.Canvas(root, width=200, height=100)
canvas.pack()

newline = canvas.create_line(0, 0, 200, 100)
otherline = canvas.create_line(100, 0, 100, 100, fill="green")

root.mainloop()
