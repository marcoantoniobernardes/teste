#1
#  coding: utf-8
from flask import Flask, render_template
app = Flask("projeto")
@app.route("/")
def ola_mundo():
    nome="Marco Antonio"
    return render_template("alo.html", n=nome), 200

app.run()