import sqlite3

db = sqlite3.connect('music.sqlite')

for songs in db.execute("SELECT * FROM songs"):
    print(songs)

db.close()
