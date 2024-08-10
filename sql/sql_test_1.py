import sqlite3

com = sqlite3.connect('database.sqlite3')

# create
# insert
# select

cursor = com.cursor() # create cursor

cursor.execute("""
               CREATE TABLE IF NOT EXISTS notebook
               (name TEXT, phone TEXT, age INTEGER)
               """)
cursor.execute("INSERT INTO notebook VALUES ('John', '555-555-5555', 30)")

com.commit()

cursor.execute("SELECT * FROM notebook")
print(cursor.fetchall())

com.close()