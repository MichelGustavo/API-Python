from flask import Flask
from main import app

# rotas

@app.route("/")
def usuarios():
    return "Meu site no flask"