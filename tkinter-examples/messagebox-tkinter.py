import tkinter
import tkinter.messagebox

root = tkinter.Tk()

tkinter.messagebox.showinfo("title", "this is awsome")

response = tkinter.messagebox.askquestion("question1", "do you like coffe?")

if response == "yes":
    tkinter.messagebox.showinfo("yessss", "here is your coffe on me!")
else:
    tkinter.messagebox.showinfo("NO!", "oh sorry for you")

root.mainloop()
