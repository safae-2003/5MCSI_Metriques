from flask import Flask, render_template, jsonify, request
from datetime import datetime
from urllib.request import urlopen
import json

app = Flask(__name__)

# ---------------- Page d'accueil ----------------
@app.route('/')
def hello_world():
    return render_template('hello.html')


# ---------------- Page Contact ----------------
@app.route('/contact/', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        print("Message reçu !")
        print("Nom :", request.form['name'])
        print("Email :", request.form['email'])
        print("Message :", request.form['message'])
        return render_template("contact.html", success=True)
    return render_template("contact.html", success=False)


# ---------------- Tawarano JSON API (Commits modèle) ----------------
@app.route('/tawarano/')
def tawarano():
    url = "https://api.github.com/repos/OpenRSI/5MCSI_Metriques/commits"
    response = urlopen(url)
    data = json.loads(response.read().decode("utf-8"))

    result = []
    for item in data:
        date = item["commit"]["author"]["date"][5:10]  # MM-DD
        minutes = int(item["commit"]["author"]["date"][14:16])
        result.append({"date": date, "temp": minutes})

    return jsonify(result)


# ---------------- Page Graphique ----------------
@app.route("/rapport/")
def rapport():
    return render_template("graphique.html")


# ---------------- Page Histogramme ----------------
@app.route("/histogramme/")
def histogramme():
    return render_template("histogramme.html")


# ---------------- 🔥 NOUVEAU : API Spotify Exercice 6 ----------------
@app.route('/api/spotify/')
def api_spotify():
    data = [
        {"titre": "Calm Down", "artiste": "Rema", "annee": 2022},
        {"titre": "Sprinter", "artiste": "Dave & Central Cee", "annee": 2023},
        {"titre": "Flowers", "artiste": "Miley Cyrus", "annee": 2023},
        {"titre": "People", "artiste": "Libianca", "annee": 2023}
    ]
    return jsonify(data)


# ---------------- Page Spotify (tableau) Exercice 6 ----------------
@app.route('/spotify/')
def spotify_page():
    return render_template('spotify.html')


# ---------------- Lancement du serveur ----------------
if __name__ == "__main__":
    app.run(debug=True)
