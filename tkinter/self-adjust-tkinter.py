import tkinter

root = tkinter.Tk()

label1 = tkinter.Label(root, text="first", bg="red", fg="white")
label1.pack(fill="x")

label2 = tkinter.Label(root, text="second", bg="blue", fg="black")
label2.pack(side="left", fill="y")


root.mainloop()
