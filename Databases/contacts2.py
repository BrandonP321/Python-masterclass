import sqlite3

db = sqlite3.connect("contacts.sqlite")

new_email = 'anewemail@update.com'
phone = input("Please enter your phone number: ")

# update_sql = f"UPDATE contacts SET email = '{new_email}' WHERE phone = {phone}"
update_sql = f"UPDATE contacts SET email = ? WHERE phone = ?"
print(update_sql)
update_cursor = db.cursor()

# below is the use of placeholders: .execute(<sql code>, <tuple of replacement values separated by ','s)
update_cursor.execute(update_sql, (new_email, phone))

print(f"{update_cursor.rowcount} rows updated.")

update_cursor.connection.commit()  # commits code written within the cursor rather than the whole database

update_cursor.close()

for name, phone, email in db.execute("SELECT * FROM contacts"):
    print(name)
    print(phone)
    print(email)
    print('*' * 20)

db.close()
