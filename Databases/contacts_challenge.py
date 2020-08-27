import sqlite3

db = sqlite3.connect('contacts.sqlite')

name = input('What is your name: ')

for row in db.execute("SELECT * FROM contacts WHERE name LIKE ?", (name,)):  # ',' is needed to make it a tuple
    print(row)
# using 'LIKE' makes the search case in-sensitive

db.close()
