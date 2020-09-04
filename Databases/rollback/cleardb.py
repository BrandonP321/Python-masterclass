import sqlite3

db = sqlite3.connect("accounts.sqlite")

db.execute("DROP TABLE accounts")
db.execute("DROP TABLE history")

db.close()
