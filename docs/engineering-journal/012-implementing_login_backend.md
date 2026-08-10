## Implementing the Smart Wallet Registration Backend

**Engineering Journal - Entry 011**

**Date:** 8 August 2026

### Today's Goal

Implement the backend registration flow for Smart Wallet and connect the registration form with the SQLite database so that users can securely create accounts and have their information permanently stored.

### What I Learned

- Learned how Flask handles form submissions using `POST` requests.
- Understood how `request.form` is used to retrieve data submitted through an HTML form.
- Learned how to validate user input before storing it in the database.
- Implemented checks to ensure that all registration fields are filled.
- Learned how to check whether an email already exists in the database using a parameterized SQL `SELECT` query.
- Understood why parameterized SQL queries using `?` are safer than directly inserting user input into SQL statements.
- Implemented password confirmation checking to ensure that both password fields contain the same value.
- Added password-strength requirements including minimum length, uppercase letters, lowercase letters, numbers, and special characters.
- Learned how bcrypt is used to securely hash passwords before storing them.
- Understood that bcrypt generates a unique salt for passwords, meaning identical passwords do not result in identical stored hashes.
- Learned that the original password should never be stored directly in the database.
- Used a parameterized SQL `INSERT` query to store the user's name, email, and hashed password.
- Learned the importance of `connection.commit()` for permanently saving database changes.
- Used `connection.close()` after completing database operations to properly release the database connection.
- Learned how Flask's `render_template()` can pass messages and errors from the backend to the HTML template.
- Used Jinja template syntax to display registration success and error messages on the registration page.

### Challenges Faced

Initially, I had several syntax and logic mistakes while building the registration route, especially with Flask request handling, SQLite imports, and password hashing. I also encountered an issue where the registration was successfully creating the account in the database, but the success message was not visible on the webpage. I learned that sending a message from Flask using `render_template()` is not enough; the HTML template must explicitly display the value using Jinja syntax.

I also had to install the `bcrypt` package in the project's virtual environment before Python could use it for password hashing.

### Key Takeaways

- Flask uses `request.form` to retrieve submitted form data.
- Backend validation should happen before inserting data into the database.
- Parameterized SQL queries help protect against SQL injection.
- Passwords should be hashed with bcrypt rather than stored as plaintext.
- `bcrypt.hashpw()` is used when creating the password hash, while `bcrypt.checkpw()` can later be used during login to verify a password.
- `connection.commit()` saves database changes permanently.
- `render_template()` can send data from Flask to an HTML template.
- Jinja variables such as `{{ message }}` allow the HTML page to display backend-generated information.

### Progress Made

- ✅ Connected the registration route to the SQLite database.
- ✅ Implemented `GET` and `POST` handling for registration.
- ✅ Retrieved registration form data using `request.form`.
- ✅ Added empty-field validation.
- ✅ Added duplicate-email checking.
- ✅ Added password-strength validation.
- ✅ Added password confirmation validation.
- ✅ Installed and integrated bcrypt.
- ✅ Implemented secure password hashing with bcrypt and salt.
- ✅ Inserted registered users into the `users` table.
- ✅ Added database commit and connection closing.
- ✅ Added registration success and error messages.
- ✅ Successfully tested the complete registration flow.
- ✅ Verified that the password was stored as a bcrypt hash instead of plaintext.
- ✅ Removed the temporary test account after testing.

### Reflection

Today's session was an important step in turning Smart Wallet from a basic Flask application into a functional application with real user accounts. I learned how the frontend registration form communicates with the backend, how the backend validates the submitted information, and how the validated data is securely stored in SQLite.

The most important part of this session was understanding that authentication is not simply about storing a password. Passwords must be protected using secure hashing, and user input must be validated before it reaches the database. I also learned how backend responses can be passed back to the frontend and displayed using Jinja.

With the registration system now working, Smart Wallet has its first complete authentication feature. The next step is to implement login, password verification, sessions, protected pages, and logout functionality.
