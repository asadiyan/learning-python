import tkinter

root = tkinter.Tk()

newFrame = tkinter.Frame(root)
newFrame.pack()

otherFrame = tkinter.Frame(root)
otherFrame.pack(side="bottom")

button1 = tkinter.Button(newFrame, text="click here", fg="red")
button2 = tkinter.Button(otherFrame, text="click here", fg="blue")

button1.pack()
button2.pack()


root.mainloop()
