from sqlite3 import connect

userDB = connect("user.db", check_same_thread=False)
cursor = userDB.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_data(
        id TEXT UNIQUE NOT NULL,
        passwd TEXT NOT NULL,
        token TEXT UNIQUE NOT NULL)
    """)
