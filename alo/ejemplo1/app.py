from flask import Flask, render_template
import random

app=Flask(__name__)

@app.route("/")
def index():
    mensajes = ['este mensaje es insano', 'que dia es hoy?', 'pau 23']
    return render_template('index.html', mensajes= mensajes)

@app.route("/imagen")
def imagen():
    return render_template('imagen.html')



