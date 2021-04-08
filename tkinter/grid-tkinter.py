import tkinter

root = tkinter.Tk()

label1 = tkinter.Label(root, text="first name")
label2 = tkinter.Label(root, text="last name")

entry1 = tkinter.Entry(root)
entry2 = tkinter.Entry(root)

label1.grid(row=0, column=0)
label2.grid(row=1, column=0)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

root.mainloop()
