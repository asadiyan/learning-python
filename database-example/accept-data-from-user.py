import psycopg2


def create():
    conn = psycopg2.connect(dbname="studentdb", user="postgres", password="example", host="localhost", port="5432")
    cur = conn.cursor()
    cur.execute("""CREATE TABLE student(ID SERIAL, NAME TEXT, AGE TEXT, ADDRESS TEXT);""")
    print("table created")
    conn.commit()
    conn.close()


def insert_data():
    conn = psycopg2.connect(dbname="studentdb", user="postgres", password="example", host="localhost", port="5432")
    cur = conn.cursor()
    name = input("enter your name:\n")
    age = input("enter your age:\n")
    address = input("enter your addres:\n")

    query = """INSERT INTO student (NAME, AGE, ADDRESS) VALUES (%s, %s, %s);"""
    cur.execute(query, (name, age, address))
    print("adding to table completed")
    conn.commit()
    conn.close()

# create() 
insert_data()
