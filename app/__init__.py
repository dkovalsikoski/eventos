from flask import Flask
from flask import render_template

app = Flask(__name__)
@app.route('/home')
def home():
    e = ['SIMPRAD', 'Semana ADS', 'Semana de Ciência e Técnologia']
    return render_template("index.html", eventos=e)
