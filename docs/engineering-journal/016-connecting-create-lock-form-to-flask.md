## Connecting the Create Lock Form to Flask

**Engineering Journal - Entry 016**

**Date:** 14 September 2026

### Today's Goal

- Continue development of the Smart Wallet project after completing the Money Locks page structure.

- Begin making the Create Lock form functional.

- Connect the HTML form to the Flask backend using a POST request.

- Verify that user-entered lock information is successfully received by Flask.

### What I Learned

- **HTML form submission:**

Added `method="POST"` to the Create Lock form so that the information entered by the user is sent to the Flask backend instead of simply loading the page.

- **GET and POST requests:**

Updated the Create Lock route to accept both `GET` and `POST` requests.

`GET` is used when displaying the Create Lock page, while `POST` is used when the user submits the form.

- **Flask `request.form`:**

Learned that Flask provides submitted HTML form data through `request.form`.

The data can be accessed using the same names given to the form inputs through their `name` attributes.

- **Testing backend communication:**

Used `print(request.form)` to verify that the data entered into the form was successfully received by Flask.

### Challenges Faced

- Initially, submitting the form appeared to do nothing on the website.

- Checked the Flask terminal and found that the POST request was successfully reaching the correct route with a `200` response.

- Realized that the Flask route was receiving the data but was not yet processing or storing it.

- Printed `request.form` to confirm that the submitted values were being received correctly.

### Key Takeaways

- An HTML form can send information to a Flask route using a POST request.

- Flask must explicitly allow POST requests through the `methods` parameter in `@app.route()`.

- The `name` attribute of an HTML form field determines the key used to access its submitted value in `request.form`.

- A successful `200` response does not necessarily mean that the application has performed the intended action; it only means the request was successfully handled.

- Testing the Flask terminal can help confirm whether data is reaching the backend.

### Progress Made

- [x] Added `method="POST"` to the Create Lock form

- [x] Updated the Create Lock route to accept GET and POST requests

- [x] Submitted test data through the form

- [x] Confirmed that Flask receives the submitted data

- [x] Verified form data using `request.form`

- [ ] Add form validation

- [ ] Store Money Lock data in SQLite

- [ ] Display dynamically created locks

- [ ] Add lock management functionality

### Reflection

Today's work was intentionally kept light so that I could restart Smart Wallet development without making the session overwhelming. Even though only a small amount of functionality was added, this was an important step because the Create Lock form is now successfully communicating with the Flask backend.

I also reinforced the difference between creating a UI and making that UI functional. The form can now send real user-entered information to Flask, but the backend does not yet process or store it.

The next step is to validate the submitted information and eventually store the Money Lock in SQLite.
