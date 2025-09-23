import sqlite3

connection = sqlite3.connect("bot_users.db")
cursor = sqlite3.Cursor(connection)

# % _ for one char
cursor.execute("SELECT * FROM users WHERE user_name LIKE ?", ("%i%",))

rows = cursor.fetchall()
for row in rows:
    print(row)

print("....................................")

# ASC & DESC
cursor.execute("SELECT * FROM users ORDER BY user_login_time DESC")

rows1 = cursor.fetchall()
for row in rows1:
    print(row)

connection.commit()
connection.close()