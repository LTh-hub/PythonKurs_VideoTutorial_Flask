# FlaskTut07_Using_SQL.py
#
# Hämtat från YouTube:
#   Flask Tutorial #7 - Using SQL Alchemy Database
#
from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = "hello"                            # Secret Key för att kunna köra login 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(days=5)  # Efter 5 dagar blir "user" utloggad

db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email



@app.route("/")
def home():
    return render_template("index_7.html")


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
        
        return render_template("login_7.html")


@app.route("/user", methods=["POST", "GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]

        if request.method == "POST":
            email=request.form["email"]
            session["email"] = email
            flash("Email was saved!")
        else:
            if "email" in session:
                email = session["email"]
        
        return render_template("user_7.html", email=email)
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    flash(f"Du har blivit utloggad!", "info")
    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for("login"))



if __name__ == "__main__":
    with app.app_context():     # För att köra db.create_all() i kontexten av app.app_context()
        db.create_all()
    app.run(debug=True)


# 🧠 Förklaring:
# with app.app_context(): skapar ett sammanhang där 
# current_app (Flask’s globala app-objekt) är tillgängligt. 
# Då fungerar db.create_all() korrekt.


