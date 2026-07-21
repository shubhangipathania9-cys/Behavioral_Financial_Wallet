## First Dynamic Webpage

**Engineering Journal - Entry 002**

**Date:** 19 July 2026

### Today's Goal

Take the first step from a Python application to a real web application by rendering my first HTML page using Flask.

### What I Learned

- Learned why Flask applications use a dedicated `templates` folder for HTML files.
- Understood the purpose of `render_template()` and how it locates and serves HTML pages to the browser.
- Learned why separating Python logic from HTML keeps the application organized, scalable, and easier to maintain.
- Understood the complete request lifecycle:
  - The browser sends a request to the Flask application.
  - Flask matches the requested route.
  - The corresponding function is executed.
  - `render_template()` searches for the requested HTML file inside the `templates` folder.
  - Flask sends the generated HTML response back to the browser.
  - The browser interprets the HTML and displays the webpage.

- Learned the difference between the browser tab title (`<title>`) and the visible webpage content (`<body>`).
- Learned the purpose of the basic HTML structure, including `<!DOCTYPE html>`, `<html>`, `<head>`, and `<body>`.

### Challenges Faced

While rendering the webpage for the first time, I encountered the following error:

`jinja2.exceptions.TemplateNotFound: index.html`

Instead of making random changes, I debugged the application step by step. After verifying the Flask route, imports, and project structure, I discovered that the issue was simply a typo in the HTML filename. Correcting the filename immediately resolved the error.

### Key Takeaways

- Error messages should be treated as guidance rather than obstacles.
- Small mistakes, such as a typo in a filename, can prevent an application from working correctly.
- Understanding the complete flow of a request is more valuable than memorizing individual lines of code.
- Organizing code into separate responsibilities makes future development easier and keeps the project maintainable.

### Progress Made

- ✅ Successfully rendered my first HTML page using Flask.
- ✅ Connected a Flask route to an HTML template.
- ✅ Learned how the browser, Flask, and HTML work together to display a webpage.
- ✅ Completed my first debugging session in Flask by identifying and fixing a filename typo.

### Reflection

Today marked the moment when Smart Wallet evolved from a Python script into the foundation of a real web application. Watching my own HTML page appear in the browser was a rewarding milestone, but solving the `TemplateNotFound` error was an equally valuable experience. It reinforced an important lesson: debugging is not about guessing—it is about understanding what the application is communicating. This milestone strengthened my confidence and gave me a clearer understanding of how browsers, Flask, and HTML interact to build a web application.
