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
    return "<h1>Welcome to Smart Wallet Dashboard!</h1>"

@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        print("Name:", name)
        print("Email:", email)
        print("Password:", password)
        print("Confirm Password:", confirm_password)

        if password != confirm_password:
            print("Passwords do not match. Please try again.")
        else:
            print("Account created successfully!")

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]
    # Temporary user (until we connect a database)

        stored_email = "test@smartwallet.com"
        stored_password = "Password123!"

        # Authentication will go here.
        if email != stored_email:               
            return render_template(
            "login.html",
            error="Invalid email or password."
            )
        if password != stored_password:
            return render_template(
            "login.html",
            error="Invalid email or password."
    )
        session["user"] = email
        return redirect(url_for("dashboard"))
    return render_template("login.html")
if __name__ == "__main__":
    app.run(debug=True)
        

