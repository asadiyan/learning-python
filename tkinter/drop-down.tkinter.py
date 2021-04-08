import tkinter


def function1():
    print("menu item clicked")


root = tkinter.Tk()

mymenu = tkinter.Menu(root)

root.config(menu=mymenu)

# creating sub menu with items inside it
submenu = tkinter.Menu(mymenu)
mymenu.add_cascade(label="file", menu=submenu)
submenu.add_command(label="project", command=function1)
submenu.add_command(label="save", command=function1)
# this function separate two items
submenu.add_separator()
submenu.add_command(label="exit", command=function1)

# creating a new menue near by the sub menu with single item
newmenu = tkinter.Menu(mymenu)
mymenu.add_cascade(label="edit", menu=newmenu)
newmenu.add_command(label="undo", command=function1)

root.mainloop()
