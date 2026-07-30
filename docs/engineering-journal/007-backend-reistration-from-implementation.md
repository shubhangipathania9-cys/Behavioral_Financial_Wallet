## Backend Registration Form Implementation

**Engineering Journal - Entry 007**

**Date:** 30 July 2026

### Today's Goal

Connect the registration form to the Flask backend, receive user input, and implement the first server-side validation by checking whether the password and confirm password fields match.

### What I Learned

- Learned how HTML forms communicate with Flask using the `action` and `method` attributes.
- Understood the difference between `GET` and `POST` requests and why `POST` is used when submitting form data.
- Learned how to configure a Flask route to accept multiple request methods using `methods=['GET', 'POST']`.
- Learned how to retrieve user-submitted data using `request.form`.
- Understood the purpose of `request.method` and how it allows Flask to distinguish between displaying a webpage and processing submitted form data.
- Implemented my first backend validation by comparing the password and confirm password fields.
- Learned how temporary `print()` statements can be used to debug backend functionality during development.
- Learned why passwords should never be displayed or stored in plain text in a real application and that they should eventually be hashed before being saved.

### Challenges Faced

After submitting the registration form, the page simply reloaded with empty fields. Initially, this seemed like an error, but after testing the application step by step, I understood that Flask was successfully receiving the data and simply rendering the registration page again because no further actions had been implemented yet.

I also noticed that the password was visible in the VS Code terminal because I had explicitly printed it for debugging. This became an important lesson about secure password handling and why temporary debugging code should later be removed.

### Key Takeaways

- Backend features should be developed and tested one small step at a time.
- `request.form` provides access to the data submitted through an HTML form.
- Temporary debugging statements are useful during development but should not remain in the final version of the application.
- Sensitive information, such as passwords, should never be displayed or stored as plain text.
- Good software is not only functional but also secure and user-friendly.

### Progress Made

- ✅ Connected the registration form to the Flask backend.
- ✅ Configured the `/register` route to handle both `GET` and `POST` requests.
- ✅ Successfully received form data from the browser.
- ✅ Implemented password confirmation validation.
- ✅ Verified backend functionality using temporary debugging statements.

### Reflection

Today marked an important milestone in the development of Smart Wallet. For the first time, the application was able to receive user input, process it on the server, and make decisions based on that data. Although the current feedback is only displayed in the terminal, this implementation lays the foundation for future features such as user authentication, database integration, and account creation. I also gained a deeper understanding that writing software is not only about making features work but also about building them securely and creating a better experience for the user.
