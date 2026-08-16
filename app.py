
from multiprocessing.dummy import connection
import sqlite3
import bcrypt
import email

from flask import Flask,render_template,request,redirect,url_for,session  

# create the main flask application

app = Flask(__name__)
app.secret_key = 'replace_this_with_a_random_secret_key'   


@app.route('/')
def home():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect(url_for("login"))
    user_id = session["user_id"]
    connection = sqlite3.connect("database/smartwallet.db")
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE id = ?",
        (user_id,)
    )
    user = cursor.fetchone()

    if user is None:
        connection.close()
        session.clear()
        return redirect(url_for("login"))

    connection.close()

    return render_template("dashboard.html", user=user)

@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]
        if not name or not email or not password or not confirm_password:
            return render_template("register.html", error="Please fill in all fields.")
        if password != confirm_password:
            return render_template("register.html", error="Passwords do not match. Please try again.")
        if len(password) < 8:
            return render_template("register.html", error="Password must be at least 8 characters long.")
        if not any(char.isdigit() for char in password):
            return render_template("register.html", error="Password must contain at least one number.")
        if not any(char.isupper() for char in password):
            return render_template("register.html", error="Password must contain at least one uppercase letter.")
        if not any(char.islower() for char in password):
            return render_template("register.html", error="Password must contain at least one lowercase letter.")
        if not any(char in "!@#$%^&*()-_=+[{]}\|;:'\",<.>/?`~" for char in password):
            return render_template("register.html", error="Password must contain at least one special character.")

        connection = sqlite3.connect("database/smartwallet.db")    
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE email=?", (email,))
        user = cursor.fetchone()
        if user is not None:
            connection.close()
            return render_template(
                "register.html",
                error="Email already exists. Please Login."
            )


        hashed_password = bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt()
        )
        cursor.execute(
            "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
            (name, email, hashed_password)
)

        connection.commit()
        connection.close()
        return render_template("register.html", message="Account created successfully!")
    return render_template("register.html")
 

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        connection = sqlite3.connect("database/smartwallet.db")
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE email = ?",
            (email,)
        )

        user = cursor.fetchone()

        if user is None:
            connection.close()
            return render_template(
                "login.html",
                error="Invalid email or password."
            )

        stored_hash = user[3]

        if bcrypt.checkpw(
            password.encode("utf-8"),
            stored_hash
        ):
            session["user_id"] = user[0]
            connection.close()
            return redirect(url_for("dashboard"))

        connection.close()
        return render_template(
            "login.html",
            error="Invalid email or password."
        )

    return render_template("login.html")
if __name__ == "__main__":
    app.run(debug=True)
        

