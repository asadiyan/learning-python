import tkinter


class MyButtons:

    def __init__(self, rootone):
        frame = tkinter.Frame(rootone)
        frame.pack()

        self.printbutton = tkinter.Button(frame, text="click here", command=self.printmessage, bg="blue")
        self.printbutton.pack()

        self.quitbutton = tkinter.Button(frame, text="Exit", command=frame.quit, bg="red")
        self.quitbutton.pack(side="left")

    def printmessage(self):
        print("button clicked")


root = tkinter.Tk()

b = MyButtons(root)

root.mainloop()
