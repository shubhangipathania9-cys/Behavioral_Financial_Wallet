## Creating the Smart Wallet Database

**Engineering Journal - Entry 010**

**Date:** 6 August 2026

### Today's Goal

Create the first SQLite database for Smart Wallet and understand how a Flask application stores persistent data instead of relying on temporary hardcoded values.

### What I Learned

- Learned what a database is and why applications need one to permanently store user information.
- Understood that SQLite is a lightweight, file-based relational database that is built into Python.
- Learned how `sqlite3.connect()` creates a new database automatically if it does not already exist and opens it if it already exists.
- Understood the purpose of a database connection and how it allows Python to communicate with the database.
- Learned what a cursor is and how it is used to execute SQL commands.
- Created the first `users` table containing the fields `id`, `name`, `email`, and `password`.
- Learned the purpose of `PRIMARY KEY` and `AUTOINCREMENT` for uniquely identifying each user.
- Understood why the `email` field should be marked as `UNIQUE` to prevent duplicate accounts.
- Learned the importance of `connection.commit()` to permanently save changes made to the database.
- Understood why `connection.close()` should be called after database operations to properly release resources.
- Learned why `CREATE TABLE IF NOT EXISTS` is used to safely handle the case where the table has already been created, making the setup script safe to run multiple times.

### Challenges Faced

Initially, I expected to manually create the database file. During the session, I learned that SQLite automatically creates the `.db` file when `sqlite3.connect()` is called if the file does not already exist. This helped me better understand how SQLite manages databases and simplified the setup process.

### Key Takeaways

- Databases allow applications to store information permanently instead of using temporary variables.
- SQLite automatically creates the database file if it does not already exist.
- A cursor acts as the interface used to execute SQL commands.
- Changes are not permanently saved until `connection.commit()` is executed.
- Using `IF NOT EXISTS` makes database initialization scripts safe to run repeatedly without generating errors.

### Progress Made

- ✅ Created the `database` folder structure for Smart Wallet.
- ✅ Created the `database.py` setup script.
- ✅ Generated the `smartwallet.db` SQLite database.
- ✅ Created the `users` table with the required fields.
- ✅ Successfully connected Python to SQLite.
- ✅ Learned the complete database creation workflow.

### Reflection

Today's session marked an important milestone because Smart Wallet now has its first real database. Instead of relying on hardcoded user information, the project is now prepared to store persistent data. More importantly, I understood the purpose of each step involved in creating the database rather than simply copying the code. This session laid the foundation for implementing user registration, login authentication, and future database-driven features.
