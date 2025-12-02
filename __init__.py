from flask import Flask, render_template, render_template_string, jsonify, request
from datetime import datetime
from urllib.request import urlopen
import json

app = Flask(__name__)

# Page d'accueil
@app.route('/')
def hello_world():
    return render_template('hello.html')

# Page de contact (Exo 2)
@app.route('/contact/')
def contact():
    return render_template('contact.html')

# Page du graphique en courbe (Exo 4)
@app.route("/rapport/")
def rapport():
    return render_template("graphique.html")

# Page de l'histogramme (Exo 5)
@app.route("/histogramme/")
def histogramme():
    return render_template("histogramme.html")

# API pour récupérer les données depuis l’API GitHub (Exo 3bis + Exo 6)
@app.route('/tawarano/')
def tawarano():
    url = "https://api.github.com/repos/OpenRSI/5MCSI_Metriques/commits"
    response = urlopen(url)
    data = json.loads(response.read().decode("utf-8"))

    result = []
    for item in data:
        # Exemple de température venant des minutes (fausse donnée mais OK pour l’exercice)
        date = item["commit"]["author"]["date"][5:10]  # Format "MM-DD"
        minutes = int(item["commit"]["author"]["date"][14:16])
        result.append({"date": date, "temp": minutes})

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
