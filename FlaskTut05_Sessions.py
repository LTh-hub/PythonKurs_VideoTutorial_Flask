# FlaskTut05_Sessions.py
#
# Hämtat från YouTube:
#   Flask Tutorial #5 - Sessions
#
from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta


app = Flask(__name__)
app.secret_key = "hello"                            # Secret Key för att kunna köra login 
app.permanent_session_lifetime = timedelta(days=5)  # Efter 5 dagar blir "user" utloggad


@app.route("/")
def home():
    return render_template("index_5.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        
        return render_template("login.html")


@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))



if __name__ == "__main__":
    app.run(debug=True)
