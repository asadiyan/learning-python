import psycopg2


# conn is a object that connect us with the database
# now if we wnat to do something with database insert,delete or create we do it by conn
conn = psycopg2.connect(dbname="studentdb", user="postgres", password="example", host="localhost", port="5432")
print("connection sucsses")


