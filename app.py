from flask import Flask

# create the main flask application

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello, Smart Wallet!"

if __name__ == '__main__':
    app.run(debug=True)

