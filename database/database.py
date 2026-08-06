import sqlite3

# Connect to the database (creates it if it doesn't exist)
connection = sqlite3.connect("database/smartwallet.db")

# Create a cursor
cursor = connection.cursor()

# Create the users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
""")

# Save changes
connection.commit()

# Close the connection
connection.close()

print("Database and users table created successfully!")