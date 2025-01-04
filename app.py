from flask import Flask, render_template
from flask_sslify import SSLify
from waitress import serve

app = Flask(__name__)
sslify = SSLify(app)


@app.route("/")
def index():
    return render_template("acceuil.html")

@app.route("/<name>")
def say_hi(name):
    return render_template("acceuil.html", name=name)

if __name__ == '__main__':
    app.run(debug=True)