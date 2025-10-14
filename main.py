from flask import Blueprint, jsonify, request
from .mo

app = Flask(__name__)

from routes import *



if __name__ == "__main__":
    app.run()