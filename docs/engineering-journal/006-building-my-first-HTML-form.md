## Building My First HTML Form

**Engineering Journal - Entry 006**

**Date:** 27 July 2026

### Today's Goal

Build the registration page for Smart Wallet while learning how HTML forms collect user information and communicate with a Flask application.

### What I Learned

- Learned the purpose of the `<form>` element and how it groups related user inputs before sending data to the backend.
- Understood the difference between collecting information using `<input>` elements and submitting it using a `<button type="submit">`.
- Learned why semantic HTML elements such as `<main>`, `<label>`, and `<form>` improve both code organization and accessibility.
- Learned how the `for` attribute in a `<label>` connects to the corresponding input's `id`, allowing users to click the label to focus the input field.
- Understood the importance of selecting appropriate input types such as `text`, `email`, and `password` instead of using generic text fields for every input.
- Learned the purpose of the `required` attribute and how it prevents incomplete form submissions on the client side.
- Learned how placeholders improve user experience by guiding users without replacing descriptive labels.
- Understood the difference between labels and placeholders:
  - Labels identify the purpose of a field.
  - Placeholders provide guidance on what information should be entered.

- Learned why consistent naming conventions (such as `confirm_password`) make backend development cleaner and easier to maintain.

### Challenges Faced

While building the registration form, I initially focused only on the primary fields and accidentally omitted the **Confirm Password** field. After reviewing the registration flow, I realized that password confirmation is an essential validation step for account creation. I also refined the form by replacing instructional labels with concise labels and moving guidance into placeholders, resulting in a cleaner and more user-friendly interface.

### Key Takeaways

- HTML forms should be built using semantic elements rather than generic containers.
- Every form field should have a descriptive label to improve accessibility.
- Different input types provide better validation and improve the user experience.
- Backend validation remains essential even when HTML provides client-side validation through attributes like `required`.
- Good user interface design focuses on clarity, consistency, and reducing unnecessary cognitive effort for users.

### Progress Made

- ✅ Created the `register.html` page for Smart Wallet.
- ✅ Built the complete registration form using semantic HTML.
- ✅ Added fields for Full Name, Email Address, Password, and Confirm Password.
- ✅ Applied appropriate input types, placeholders, labels, and required validation.
- ✅ Designed the registration page to align with Smart Wallet's calm and minimal design philosophy.
- ✅ Planned navigation between the Registration and Login pages for a smoother user experience.

### Reflection

Today's session marked my first experience building a complete HTML form from scratch. More importantly, I learned that creating forms is not just about placing input fields on a page—it involves understanding accessibility, semantic HTML, user experience, and how information eventually flows to the backend. Every design decision, from choosing meaningful labels to selecting appropriate input types, contributes to making the application easier to use and maintain. This session strengthened my understanding of frontend development and laid the foundation for connecting the registration page to Flask and the database in future sessions.
