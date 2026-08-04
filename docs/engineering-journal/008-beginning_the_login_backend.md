## Beginning the Login Backend

**Engineering Journal - Entry 008**

**Date:** 5 August 2026

### Today's Goal

Begin implementing the Smart Wallet login backend while understanding the complete authentication workflow before connecting the application to a database.

### What I Learned

- Learned why a single Flask route can handle both `GET` and `POST` requests by specifying the allowed HTTP methods.
- Understood the purpose of checking `request.method` before processing submitted form data.
- Learned how `request.form` retrieves user-entered data from the login form.
- Understood that authentication begins by identifying the user through their email before verifying their password.
- Learned why the backend first searches for the email in the database before attempting password verification.
- Understood that if the email does not exist, there is no password hash to compare against, so authentication should stop immediately.
- Learned why applications should return a generic error message such as **"Invalid email or password"** instead of revealing whether the email or password was incorrect.
- Understood how generic authentication messages help reduce the risk of user enumeration attacks.
- Reinforced that plaintext passwords should never be stored in the database and that password verification will later be performed using bcrypt hashes.
- Learned how proper indentation ensures authentication logic executes only when processing a `POST` request.

### Challenges Faced

While reasoning through the authentication flow, I initially mixed parts of the registration process with the login process. After reviewing the login algorithm step by step, I understood that login does not create or store new user credentials. Instead, it retrieves existing user information, verifies the submitted password against the stored bcrypt hash, and will later create a session after successful authentication.

### Key Takeaways

- Authentication is a sequence of clearly defined steps rather than a single password comparison.
- User identification should always occur before password verification.
- Secure applications avoid revealing whether an email address exists during login.
- Passwords should never be stored or compared in plaintext.
- Writing the algorithm before writing the code makes implementation easier to understand and reduces mistakes.

### Progress Made

- ✅ Updated the `/login` route to support both `GET` and `POST` requests.
- ✅ Retrieved login credentials using `request.form`.
- ✅ Added a temporary user to simulate authentication before integrating the database.
- ✅ Implemented the initial email validation step using a generic authentication error message.
- ✅ Reviewed and refined the complete login workflow before implementing bcrypt verification and session creation.

### Reflection

Today's session focused more on understanding than coding. Instead of rushing through authentication, I learned why each step of the login process exists and how they work together to create a secure authentication flow. Breaking the feature into smaller pieces helped me understand the purpose of every line of code instead of simply copying an implementation. This foundation will make it much easier to integrate bcrypt, sessions, and database authentication in the upcoming development sessions.
