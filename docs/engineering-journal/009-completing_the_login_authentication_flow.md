## Completing the Login Authentication Flow

**Engineering Journal - Entry 009**

**Date:** 5 August 2026

### Today's Goal

Complete the Smart Wallet login authentication flow by implementing credential validation, session creation, user redirection, and frontend error handling while testing the complete login process.

### What I Learned

- Learned how a login form communicates with the Flask backend using the `POST` method.
- Understood how Flask retrieves submitted email and password values using `request.form`.
- Learned how temporary hardcoded credentials can be used to test the authentication flow before connecting a database.
- Implemented email verification followed by password verification as part of the login process.
- Reinforced why applications should always display a generic authentication message such as **"Invalid email or password."** instead of identifying which credential is incorrect.
- Learned how Flask sessions store the authenticated user's identity after a successful login.
- Understood how `redirect()` and `url_for()` work together to send authenticated users to another page after successful login.
- Learned how to display backend error messages conditionally using Jinja templating with `{% if error %}`.
- Learned that pressing the **Enter** key inside a form automatically submits the form when a submit button is present, improving accessibility and user experience.
- Understood the difference between `type="submit"` and `type="button"` in HTML forms and how they affect form submission.

### Challenges Faced

While implementing the login system, I encountered an `AssertionError` caused by defining the `/login` route twice. After removing the duplicate route, I discovered that the Flask application still would not start because `app.run()` had been mistakenly indented inside the `login()` function. Once it was moved outside the function, the application ran successfully. During testing, I also realized that the login page only displayed a welcome message because no login form had been created yet. After building the frontend, connecting it to the backend, and displaying authentication errors through Jinja templates, I successfully tested the complete login workflow.

### Key Takeaways

- Authentication combines frontend forms, backend validation, sessions, and page redirection into one complete workflow.
- Generic authentication messages improve security by reducing the risk of user enumeration attacks.
- Flask sessions allow applications to remember authenticated users without storing sensitive information such as passwords.
- Jinja templates enable dynamic communication between the backend and frontend.
- Careful attention to route definitions and Python indentation is essential for building reliable Flask applications.

### Progress Made

- ✅ Created the complete `login.html` page.
- ✅ Added Email Address and Password input fields.
- ✅ Connected the login form to the Flask backend.
- ✅ Implemented temporary authentication using hardcoded credentials.
- ✅ Added generic authentication error handling.
- ✅ Displayed backend error messages using Jinja templating.
- ✅ Created a session after successful authentication.
- ✅ Redirected authenticated users to the Smart Wallet dashboard.
- ✅ Successfully tested invalid email, invalid password, and successful login scenarios.

### Reflection

Today's session marked the completion of my first working authentication system in Flask. Instead of only learning the theory, I implemented the complete login workflow and successfully connected the frontend with the backend. Along the way, I resolved routing, indentation, and frontend issues, reinforcing the importance of debugging and understanding the application flow. This implementation provides a strong foundation for replacing the temporary credentials with a database and secure bcrypt password verification in future development.
