import psycopg2

conn = psycopg2.connect(dbname="studentdb", user="postgres", password="example", host="localhost", port="5432")
cur = conn.cursor()
cur.execute("""CREATE TABLE student(ID SERIAL, NAME TEXT, AGE TEXT, ADDRESS TEXT);""")
print("table created")
conn.commit()
conn.close()
