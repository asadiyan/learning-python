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

# toolbar implementation starts here
toolbar = tkinter.Frame(root, bg="pink")
insertbutton = tkinter.Button(toolbar, text="insert files", command=function1)
insertbutton.pack(side="left", padx=2, pady=3)

printbutton = tkinter.Button(toolbar, text="print", command=function1)
printbutton.pack(side="left", padx=2, pady=3)

toolbar.pack(side="top", fill="x")

# here we implement the status bar 
statusbar = tkinter.Label(root, text="this is the status", bd=1, relief="sunken", anchor="w")
statusbar.pack(side="bottom", fill="x")

root.mainloop()

