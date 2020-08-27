import sqlite3

db = sqlite3.connect("contacts.sqlite")  # connects to/creates database 'contacts.sqlite'
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")  # executes the code
# tables will now only be created if one of the same name doesn't exist due to 'IF NOT EXISTS'
db.execute("INSERT INTO contacts(name, phone, email) VALUES('Brandon', 6716723, 'brandon.phillips976@gmail.com')")
db.execute("INSERT INTO contacts VALUES('BRIAN', 1234, 'brian@myemail.com')")

cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")
for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)
    print("*" * 20)

cursor.close()
db.commit()
db.close()  # closes off the database connection
