from flask import Flask, render_template, jsonify, request
from datetime import datetime
from urllib.request import urlopen
import sqlite3

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')

# ---- Route page Contact (formulaire) ----
@app.route('/contact/', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        print("Message reçu !")
        print("Nom :", request.form['name'])
        print("Email :", request.form['email'])
        print("Message :", request.form['message'])
        return render_template("contact.html", success=True)

    return render_template("contact.html", success=False)

# ---- Route Graphique ----
@app.route("/rapport/")
def mongraphique():
    return render_template("graphique.html")

# ---- Route Histogramme ----
@app.route("/histogramme/")
def histogramme():
    return render_template("histogramme.html")


# ---- API : Extraire des minutes d'une date (EXO 6) ----
@app.route('/extract-minutes/<date_string>')
def extract_minutes(date_string):
    date_object = datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%SZ')
    minutes = date_object.minute
    return jsonify({'minutes': minutes})

if __name__ == "__main__":
    app.run(debug=True)
