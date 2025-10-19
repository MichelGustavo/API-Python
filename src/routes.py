from flask import Blueprint, jsonify, request
from models import create_user, get_all_users, get_user_by_id
from flask import render_template

bp = Blueprint('users', __name__)

@bp.route('/createUser')
def createUser():
    return render_template("createUser.html")

@bp.route('/users', methods=['GET'])
def list_users():
    users = get_all_users()
    return jsonify(users), 200

@bp.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    if not data or "name" not in data or "email" not in data:
        return jsonify({"error": "Campos 'name' e 'email' são obrigatórios."}), 400
    user = create_user(data)
    return jsonify(user), 201

@bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = get_user_by_id(user_id)
    if not user:
        return jsonify({"error": "Usuário não encontrado"}), 404
    return jsonify(user), 200