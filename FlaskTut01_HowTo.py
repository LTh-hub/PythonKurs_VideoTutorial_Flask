# FlaskTut01_HowTo.py
#
# Hämtat från YouTube:
#   Flask Tutorial #  1 - How to make web sites with Python
#
from flask import Flask, redirect, url_for


app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, this is my web site <h1>Hello</h1>"

@app.route("/<name>")
def user(name):
    return f"Hello {name}" 

@app.route("/admin")
def admin():
    return redirect(url_for("home"))



if __name__ == "__main__":
    app.run(debug=True)
