import sqlite3

# Create an in-memory SQLite database
connection = sqlite3.connect(":memory:")
cursor = connection.cursor()

# Create a table for storing user information
cursor.execute("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email_address TEXT,
        uuid TEXT,
    )
""")


connection.close()