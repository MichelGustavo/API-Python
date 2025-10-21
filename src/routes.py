from flask import Blueprint, jsonify, request, render_template
from models import (
    create_user,
    get_all_users,
    get_user_by_id,
    update_user,
    delete_user
)

bp = Blueprint('users', __name__)

# HTML
@bp.route('/createUser')
def createUser():
    return render_template("createUser.html")
# Página para listar usuários
@bp.route('/listUsers')
def listUsers():
    return render_template("listUsers.html")


# Página para editar usuário
@bp.route('/editUser/<int:user_id>')
def editUser(user_id):
    return render_template("editUser.html", user_id=user_id)


# HTTP API

# Listar todos
@bp.route('/users', methods=['GET'])
def list_users():
    users = get_all_users()
    return jsonify(users), 200


# Criar novo
@bp.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    if not data or not all(k in data for k in ("name", "email", "cargo")):
        return jsonify({"error": "Dados inválidos"}), 400
    user = create_user(data)
    return jsonify(user), 201


# Buscar por ID
@bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = get_user_by_id(user_id)
    if not user:
        return jsonify({"error": "Usuário não encontrado"}), 404
    return jsonify(user), 200


# Atualizar
@bp.route('/users/<int:user_id>', methods=['PUT'])
def edit_user(user_id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "Dados inválidos"}), 400
    user = update_user(user_id, data)
    if not user:
        return jsonify({"error": "Usuário não encontrado"}), 404
    return jsonify(user), 200


# Deletar
@bp.route('/users/<int:user_id>', methods=['DELETE'])
def remove_user(user_id):
    user = delete_user(user_id)
    if not user:
        return jsonify({"error": "Usuário não encontrado"}), 404
    return jsonify({"message": "Usuário removido com sucesso"}), 200

