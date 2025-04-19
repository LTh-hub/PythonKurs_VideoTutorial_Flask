# FlaskTut03_Bootstrap.py
#
# Hämtat från YouTube:
#   Flask Tutorial #  3 - Adding Bootstrap and Template Inheritance
#
#   Testa i browsern
#                   http://127.0.0.1:5000           # visar index_3.html
#                   http://127.0.0.1:5000/test      # visar new.html
#
from flask import Flask, redirect, url_for, render_template


app = Flask(__name__)



@app.route("/")
def home():
    return render_template("index_3.html")


@app.route("/test")
def test():
    return render_template("new.html")



if __name__ == "__main__":
    app.run(debug=True)
