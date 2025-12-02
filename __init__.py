from flask import Flask, render_template, jsonify
import json
from datetime import datetime
from urllib.request import urlopen

app = Flask(__name__)

# Route principale - page d'accueil
@app.route('/')
def hello_world():
    return render_template('hello.html')


# Route exercice 2 : page contact
@app.route('/contact/')
def contact():
    return render_template('contact.html')


# Route exercice 3 : API météo (Tawarano)
@app.route('/tawarano/')
def meteo():
    response = urlopen('https://samples.openweathermap.org/data/2.5/forecast?lat=0&lon=0&appid=xxx')
    raw_content = response.read()
    json_content = json.loads(raw_content.decode('utf-8'))
    results = []
    for list_element in json_content.get('list', []):
        dt_value = list_element.get('dt')
        temp_day_value = list_element.get('main', {}).get('temp') - 273.15  # Conversion Kelvin → °C
        results.append({'Jour': dt_value, 'temp': temp_day_value})
    return jsonify(results=results)


# Route exercice 3 BIS : affichage du graphique
@app.route("/rapport/")
def mongraphique():
    return render_template("graphique.html")


# Route exercice 4 : histogramme
@app.route("/histogramme/")
def histogramme():
    return render_template("histogramme.html")


if __name__ == "__main__":
    app.run(debug=True)
