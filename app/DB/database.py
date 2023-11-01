from sqlite3 import connect

userDB = connect("user.db", check_same_thread=False)
userDBCursor = userDB.cursor()

chatDB = connect("chat.db", check_same_thread=False)
chatDBCursor = chatDB.cursor()

userDBCursor.execute("""
    CREATE TABLE IF NOT EXISTS user_data(
        id TEXT UNIQUE NOT NULL,
        passwd TEXT NOT NULL,
        token TEXT UNIQUE NOT NULL)
    """)

chatDBCursor.execute("""
    CREATE TABLE IF NOT EXISTS chat_data(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        chat TEXT NOT NULL)
    """)
