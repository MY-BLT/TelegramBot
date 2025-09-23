import sqlite3

connection = sqlite3.connect("bot_users.db")
cursor = sqlite3.Cursor(connection)

cursor.execute("UPDATE users SET user_name = ? WHERE user_name = ?", ("yasin", "Ali"))
cursor.execute("DELETE from users WHERE user_id = ?", (3,))
# BETWEEN
cursor.execute("SELECT user_id, user_name, user_age from users WHERE user_age < ?", (21,))

rows = cursor.fetchall()

for row in rows:
    print(row)
    
connection.commit()
connection.close()