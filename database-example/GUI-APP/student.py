import tkinter as tk
import psycopg2


root = tk.Tk()

# this function is add buttom`s command function to connect with data base
# and add all entry part in ui app


def get_data(name, age, address):
    conn = psycopg2.connect(dbname="studentdb", user="postgres", password="example", host="localhost", port="5432")
    cur = conn.cursor()
    query = """INSERT INTO student (NAME, AGE, ADDRESS) VALUES (%s, %s, %s);"""
    cur.execute(query, (name, age, address))
    print("data inserted")
    conn.commit()
    conn.close()


# this function is the command of search button and gets id from user
# and return`s the whole row of that id


def search(id):
    conn = psycopg2.connect(dbname="studentdb", user="postgres", password="example", host="localhost", port="5432")
    cur = conn.cursor()
    query = """select * from student where id=%s"""
# now we have the result inside the cur
    cur.execute(query, (id))
# to get the data from cur we use "cur.fetch" as we only want one single
# line we use "cur.fetchone"
    row = cur.fetchone()
    print(row)
    display_search(row)
    conn.commit()
    conn.close()


# display_serach() function create a listbox and print`s our result inside it


def display_search(row):
    listbox = tk.Listbox(frame, width=20, height=1)
    listbox.grid(row=9, column=1)
    listbox.insert("end", row)


# implementing canvas to our app
canvas = tk.Canvas(root, height=480, width=900)
canvas.pack()

# adding frame to our app
frame = tk.Frame()
frame.place(relx=0.3, rely=0.1, relwidth=0.8, relheight=0.8)

# adding Add data label
label = tk.Label(frame, text="Add data")
label.grid(row=0, column=1)

# adding name label and it`s entry
label = tk.Label(frame, text="Name:")
label.grid(row=1, column=0)
entry_name = tk.Entry(frame)
entry_name.grid(row=1, column=1)

# adding age label and it`s entry
label = tk.Label(frame, text="Age:")
label.grid(row=2, column=0)
entry_age = tk.Entry(frame)
entry_age.grid(row=2, column=1)

# adding address label and it`s entry
label = tk.Label(frame, text="Address:")
label.grid(row=3, column=0)
entry_address = tk.Entry(frame)
entry_address.grid(row=3, column=1)

# adding buttom wich gets all entry`s in top and adding them to the database
# this buttom uses a function to connect with database
add_button = tk.Button(frame, text="ADD", command=lambda: get_data(entry_name.get(), entry_age.get(), entry_address.get()))
add_button.grid(row=4, column=1)

# adding label to start of search section under the ADD buttom
label = tk.Label(frame, text="Search Data")
label.grid(row=5, column=1)

# addind search label and it`s entry
label = tk.Label(frame, text="Search By ID:")
label.grid(row=6, column=0)
entry_id = tk.Entry(frame)
entry_id.grid(row=6, column=1)

# search button get`s the entry of search by id and connect`s to a function
search_button = tk.Button(frame, text="Search", command=lambda: search(entry_id.get()))
search_button.grid(row=6, column=2)

root.mainloop()
