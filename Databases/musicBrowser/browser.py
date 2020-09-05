import sqlite3

db = sqlite3.connect('music.db')

for songs in db.execute("SELECT * FROM songs"):
    print(songs)

db.close()
