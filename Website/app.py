from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def layout():
    return render_template("layout.html")

@app.route("/research", methods=["GET","POST"])
def research():
    return render_template("research.html")