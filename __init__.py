from flask import Flask, render_template, render_template_string, jsonify
from flask import render_template
import json
from datetime import datetime
from urllib.request import urlopen
import sqlite3

app = Flask(__name__)

# Route accueil
@app.route('/')
def hello_world():
    return render_template('hello.html')

# Route contact (Exercice 2)
@app.route("/contact/")
def MaPremiereAPI():
    return "<h2>Ma page de contact</h2>"

# Route Tawarano (Exercice 3)
@app.route('/tawarano/')
def meteo():
    response = urlopen('https://samples.openweathermap.org/data/2.5/forecast?lat=0&lon=0&appid=xxx')
    raw_content = response.read()
    json_content = json.loads(raw_content.decode('utf-8'))
    results = []
    for list_element in json_content.get('list', []):
        dt_value = list_element.get('dt')
        temp_day_value = list_element.get('main', {}).get('temp') - 273.15 # Kelvin -> °C
        results.append({'Jour': dt_value, 'temp': temp_day_value})
    return jsonify(results=results)

# Route rapport graphique (Exercice 3 Bis)
@app.route('/rapport/')
def mongraphique():
    return render_template("graphique.html")

# Route histogramme (Exercice 4)
@app.route('/histogramme/')
def histogramme():
    return render_template("histogramme.html")

if __name__ == "__main__":
    app.run(debug=True)
