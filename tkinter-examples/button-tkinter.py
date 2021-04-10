import tkinter

root = tkinter.Tk()


def dosomething():
    print("you clicked the button")


button1 = tkinter.Button(root, text="click here", command=dosomething)
button1.pack()

root.mainloop()
