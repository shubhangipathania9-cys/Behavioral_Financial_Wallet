## Building the Money Locks Page Structure

**Engineering Journal - Entry 015**

**Date:** 2 September 2026

### Today's Goal

- Continue development of the Smart Wallet project after completing the Dashboard UI.
- Create the dedicated Money Locks page.
- Connect the Dashboard's Money Locks section to the new page.
- Create the initial Create New Lock page.
- Establish the navigation structure for future Money Lock functionality.

### What I Learned

- **Flask route organization:**
  Learned that different pages of a Flask application can have their own routes and that the URL structure can be organized according to the application's architecture.

- **Nested Flask routes:**
  Instead of using a separate `/money-locks` route, I decided to use:
  `/dashboard/money-locks`
  This keeps the application's URLs organized around the dashboard.

- **Jinja `url_for()`:**
  Used `url_for()` in HTML to generate links to Flask routes instead of manually writing URLs. This makes navigation easier to maintain if routes change later.

- **Template navigation:**
  Learned how one HTML page can link to another Flask-rendered template through a route.

- **Authentication protection:**
  The Money Locks and Create Lock routes check whether `user_id` exists in the session before allowing access.

- **Debugging template errors:**
  Encountered a `TemplateNotFound` error because the file was accidentally named `create_locks.html` instead of `create_lock.html`. This helped reinforce the importance of matching Flask's `render_template()` filename exactly with the actual template filename.

### Challenges Faced

- Initially, the Money Locks page redirected to the login page because the session was not active.
- Had to verify that the `user_id` session variable used by the login system matched the variable checked by the new routes.
- Encountered a `TemplateNotFound` error caused by a small filename mismatch.
- The issue was fixed by correcting the template filename.

### Key Takeaways

- Flask routes and HTML templates must be connected correctly for navigation to work.
- `url_for()` is preferable to hardcoding application URLs.
- Small naming mistakes can cause runtime errors, so filenames and route names need to be checked carefully.
- Building the application feature-by-feature makes it easier to test and debug each part.

### Progress Made

- [x] Created `money_locks.html`
- [x] Added the `/dashboard/money-locks` Flask route
- [x] Connected the Dashboard's **View All** button to Money Locks
- [x] Created `create_lock.html`
- [x] Added the `/dashboard/money-locks/create` route
- [x] Connected **Create New Lock** to the Create Lock page
- [x] Verified the navigation between pages
- [ ] Add functionality to the Create Lock form
- [ ] Connect Money Locks to SQLite
- [ ] Add lock creation and management functionality

### Reflection

Today's work was mainly about building the structure of the Money Locks feature rather than implementing its backend functionality. I also realized that I want to understand the concepts behind the code instead of simply copying it. Going forward, I will continue using complete code when building features, but I will also learn the new concepts introduced with each feature so that I understand how Smart Wallet works internally.

The next step is to make the Create Lock form functional and introduce form submission, validation, and eventually database storage.
