# FlaskTut06_MessageFlashing.py
#
# Hämtat från YouTube:
#   Flask Tutorial #6 - Message Flashing
#
from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta


app = Flask(__name__)
app.secret_key = "hello"                            # Secret Key för att kunna köra login 
app.permanent_session_lifetime = timedelta(days=5)  # Efter 5 dagar blir "user" utloggad


@app.route("/")
def home():
    return render_template("index_6.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        flash("Login succesful")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already logged in!")
            return redirect(url_for("user"))
        
        return render_template("login_6.html")


@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("user.html", user=user)
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    flash(f"Du har blivit utloggad!", "info")
    session.pop("user", None)
    return redirect(url_for("login"))



if __name__ == "__main__":
    app.run(debug=True)
