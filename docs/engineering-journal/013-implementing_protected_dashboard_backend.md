## Implementing the Smart Wallet Protected Dashboard Backend

**Engineering Journal - Entry 013**

**Date:** 13 August 2026

### Today's Goal

Implement the backend foundation for the Smart Wallet dashboard by connecting it with the authenticated user's Flask session and SQLite database so that only logged-in users can access the dashboard and their corresponding user information can be retrieved securely.

### What I Learned

- Learned how Flask sessions can be used to determine whether a user is authenticated.
- Implemented a session check to prevent unauthenticated users from accessing the dashboard.
- Learned how to retrieve the logged-in user's database ID using `session["user_id"]`.
- Understood how the session and database work together during authentication.
- Used the user ID stored in the session to search for the corresponding user in the SQLite database.
- Used a parameterized SQL `SELECT` query to safely retrieve the logged-in user's record.
- Learned how `cursor.fetchone()` retrieves the matching user record from the database.
- Learned how to handle situations where the user ID stored in the session does not correspond to a database record.
- Implemented `session.clear()` to remove an invalid authentication session.
- Learned how `render_template()` can pass the retrieved user record from the backend to `dashboard.html`.
- Understood that authentication state should be stored in the session while the user's actual information is retrieved from the database.
- Learned that protected routes should verify authentication before providing access to private user information.

### Challenges Faced

Initially, the dashboard route only returned a static welcome message and did not check whether the user was authenticated. I implemented a session check so that users who are not logged in are redirected to the login page.

I also had to connect the user's session ID with the SQLite database. The session stores the authenticated user's database ID, which can then be used to retrieve the complete user record from the `users` table.

During implementation, I accidentally called `fetchone()` twice. I learned that `fetchone()` retrieves the next available row from the query result, so calling it twice can cause the second call to return `None`. I corrected this by retrieving the user record only once.

I also tested the protected dashboard in an InPrivate browser to make sure that a user without an active session could not access the dashboard. The dashboard correctly redirected the unauthenticated user to the login page.

### Key Takeaways

- Flask sessions can be used to maintain authentication state between requests.
- Protected routes should check whether the required session information exists before allowing access.
- The user's database ID can be stored in the session instead of sensitive information such as passwords.
- Parameterized SQL queries should be used when retrieving user information from the database.
- `cursor.fetchone()` retrieves a single matching database record.
- An invalid or missing user record should be handled safely.
- `session.clear()` can remove an invalid authentication session.
- `render_template()` allows backend data to be passed to the frontend.
- Authentication and database retrieval are separate steps that work together to personalize protected pages.

### Progress Made

- ✅ Added `session["user_id"]` after successful login.
- ✅ Created the `/dashboard` route.
- ✅ Added authentication protection to the dashboard.
- ✅ Tested direct dashboard access without authentication.
- ✅ Confirmed that unauthenticated users are redirected to `/login`.
- ✅ Retrieved the authenticated user's ID from the Flask session.
- ✅ Connected the dashboard route to the SQLite database.
- ✅ Used the session ID to retrieve the corresponding user.
- ✅ Added handling for an invalid or missing user record.
- ✅ Added `session.clear()` for invalid sessions.
- ✅ Closed the database connection after retrieving the user.
- ✅ Passed the user record to `dashboard.html`.
- ⬜ Display the logged-in user's information in the dashboard frontend.
- ⬜ Implement logout functionality.

### Reflection

Today's session was an important step in making Smart Wallet a properly authenticated application. I learned that simply creating a login system is not enough; private pages also need to verify that the user has an active authenticated session.

The most important part of today's session was understanding how the Flask session and SQLite database work together. The session stores the ID of the authenticated user, while the database provides the user's actual information. This allows the dashboard to identify and retrieve information for the correct user without storing sensitive information in the session.

I also learned the importance of testing protected routes independently. Testing the dashboard from an InPrivate browser helped confirm that users without an active session are correctly redirected to the login page.

With the protected dashboard backend now working, the next step is to connect the retrieved user information to the dashboard frontend and display personalized information for the logged-in user.
