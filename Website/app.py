from flask import Flask, render_template, request, redirect
import csv
from search import datafinder

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def layout():
    return render_template("home.html")

@app.route("/resources", methods=["GET","POST"])
def resources():

    with open("results.csv", "r") as file:
        reader = csv.reader(file)
        data = file.readlines()
        most_recent = data[-1]
        resource_sites = most_recent
       

    return render_template("resources.html", resource_list= resource_sites)

@app.route("/form", methods=["GET","POST"])
def form():
        return render_template("form.html")

@app.route('/research', methods=["GET","POST"])
def research():
    return render_template("research.html")

@app.route("/results", methods=["POST"])
def results():

    if request.method == "POST":

        country = str(request.form.get("country"))
        age = int(request.form.get("age"))
        city = str(request.form.get("City"))
        ethnicity = request.form.getlist("ethnicity")

        with open("results.csv", "a") as file:
            writer = csv.writer(file)
            data = [country,age,city,ethnicity]
            writer.writerow(data)
        
        return render_template("results.html")


