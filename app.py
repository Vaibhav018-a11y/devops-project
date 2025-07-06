from flask import Flask

app = Flask(name)

@app.route("/info")
def lwinfo():
        return "I am Lw from India"

@app.route("/phone")
def lwphone():
        return "787894466545643"

app.run(host="0.0.0.0")