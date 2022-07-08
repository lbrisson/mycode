#!/usr/bin/env python3
"""DEMO: receiving JSON"""

from flask import Flask, render_template
from flask import request
from flask import redirect
from flask import jsonify

import json

app= Flask(__name__)

animaldata= [{
    "name": "Lion",
    "desc": "King of the Jungle",
    "abilities": [
        "powerful bite",
        "strength",
        "strong claws",
              ]
             }]

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == 'POST':
        data = request.json
        if data:
           data= json.loads(data)
           name = data["name"]
           desc = data["desc"]
           abilities = data["abilities"]
           animaldata.append({"name":name,"desc":desc,"abilities":abilities})

    return jsonify(animaldata)

@app.route("/dolphin")
def hello_dolphin():
    return "Dolphins swim fast..."

@app.route("/hippo")
def hippo():
    return render_template("hippo.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
