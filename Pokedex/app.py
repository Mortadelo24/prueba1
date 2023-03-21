import requests

from flask import Flask, jsonify, render_template, redirect, request


app = Flask(__name__)


@app.route("/")
def index():
   
    
    return render_template('index.html')



@app.route("/p")
def p():
    res = requests.get("https://pokeapi.co/api/v2/pokemon/"+str(1))
    if res.status_code != 200:
            raise Exception("ERROR: API request unsuccessful.")
    data = res.json()
   
    
    return data




@app.route("/pokeapi")
def pokeapi():
    p = request.args.get("pokemon")
   
    res = requests.get("https://pokeapi.co/api/v2/pokemon/"+str(p))
    if res.status_code != 200:
            raise Exception("ERROR: API request unsuccessful.")
    data = res.json()
   
    name = data["name"]
    altura = data["height"]
    peso = data["weight"]
    tipo = data["types"][0]["type"]["name"]
    idp = data["id"]
    img = data["sprites"]["front_default"]
    
    

    
     
    
    return render_template('index.html',  name= name, altura=altura, peso=peso, tipo =tipo, id=idp, img= img)