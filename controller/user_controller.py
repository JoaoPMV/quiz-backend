from flask import request, jsonify, g
from sqlalchemy.exc import IntegrityError
from services.user_service import create_user, get_all_users, authenticate_user, generate_reset_token, reset_password_with_token, delete_user_by_id
from services.email_service import send_reset_email


def register_user():
    data = request.get_json(silent=True) or {}

    firstName = data.get("firstName")
    middleName = data.get("middleName")
    lastName = data.get("lastName")
    email = (data.get("email") or "").strip().lower()
    password = data.get("password")

    if not firstName or not lastName or not email or not password:
        return jsonify({"erro": "Campos obrigatórios: firstName, lastName, email, password"}), 400

    try:
        user = create_user(firstName, middleName, lastName, email, password)
        return jsonify({"mensagem": "Usuário criado com sucesso", "user": user.to_dict()}), 201
    except IntegrityError:
        return jsonify({"erro": "Email já cadastrado"}), 409
    except Exception as e:
        return jsonify({"erro": "Erro interno", "detalhe": str(e)}), 500

def list_users():
    try:
        users = get_all_users()
        return jsonify([u.to_dict() for u in users]), 200
    except Exception as e:
        return jsonify({"erro": "Erro interno", "detalhe": str(e)}), 500  


def login_user():
    data = request.get_json(silent=True) or {}
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"erro": "Email e senha são obrigatórios"}), 400

    result = authenticate_user(email, password)

    if not result:
        return jsonify({"erro": "Email ou senha inválidos"}), 401

    return jsonify(result), 200

def forgot_password():
    data = request.get_json(silent=True) or {}
    email = (data.get("email") or "").strip().lower()

    if not email:
        return jsonify({"erro": "Email is required"}), 400

    token = generate_reset_token(email)

    if not token:
        return jsonify({"mensagem": "If the email exists, instructions were sent"}), 200

    try:
        send_reset_email(email, token)
    except Exception as e:
        print("ERRO SMTP forgot_password:", repr(e))
        return jsonify({"erro": "Failed to send email"}), 500

    return jsonify({"mensagem": "If the email exists, instructions were sent"}), 200


def reset_password():
    data = request.get_json(silent=True) or {}
    token = data.get("token")
    new_password = data.get("newPassword")

    if not token or not new_password:
        return jsonify({"erro": "token e newPassword são obrigatórios"}), 400

    if len(new_password) < 6:
        return jsonify({"erro": "A nova senha deve ter pelo menos 6 caracteres"}), 400

    result = reset_password_with_token(token, new_password)

    if not result["ok"]:
        return jsonify({"erro": result["erro"]}), 400

    return jsonify({"mensagem": "Senha redefinida com sucesso"}), 200


def delete_user(user_id):
    current_user = g.current_user

    if current_user.id != user_id:
        return jsonify({"erro": "Você só pode deletar sua própria conta"}), 403

    try:
        result = delete_user_by_id(user_id)

        if not result["ok"]:
            return jsonify({"erro": result["erro"]}), 404

        return jsonify({"mensagem": "Usuário deletado com sucesso"}), 200
    except Exception:
        return jsonify({"erro": "Erro interno"}), 500