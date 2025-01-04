from flask import Flask, render_template
from flask_sslify import SSLify
from datetime import date
import pytz

app = Flask(__name__)
sslify = SSLify(app)

today = date.today()

@app.route("/")
def index():
    return render_template("acceuil.html")

@app.route("/<name>")
def say_hi(name):
    return render_template("acceuil.html", name=name)

if __name__ == '__main__':
    app.run(debug=True)