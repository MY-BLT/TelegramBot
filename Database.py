import sqlite3

connection = sqlite3.connect("bot_users.db")

cursor = sqlite3.Cursor(connection)

cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_name TEXT,
        user_family TEXT,
        user_age INTEGER,
        user_login_time DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    '''
)

# cursor.execute(
#     '''
#     INSERT INTO users (user_name, user_family, user_age) values (?, ? , ?)
#     '''
#     , ("Yasin", "Loghmani", 20)
# )
# cursor.execute(
#     '''
#     INSERT INTO users (user_name, user_family, user_age) values (?, ? , ?)
#     '''
#     , ("Ali", "Ahmadi", 22)
# )
# cursor.execute(
#     '''
#     INSERT INTO users (user_name, user_family, user_age) values (?, ? , ?)
#     '''
#     , ("Amir", "Khosro", 21)
# )

cursor.execute("SELECT user_name, user_family FROM users")
row = cursor.fetchall()

for r in row:
    print(r)

connection.commit()
connection.close()