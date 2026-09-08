from functools import wraps
from flask import request, jsonify, current_app, g
import jwt
from models.user import db, User

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization", "")

        if not auth_header.startswith("Bearer "):
            return jsonify({"erro": "Token não informado"}), 401

        token = auth_header.split(" ")[1]

        try:
            payload = jwt.decode(
                token,
                current_app.config["SECRET_KEY"],
                algorithms=["HS256"]
            )

            user = db.session.get(User, payload.get("user_id"))
            if not user:
                return jsonify({"erro": "Usuário não encontrado"}), 401

            g.current_user = user

        except jwt.ExpiredSignatureError:
            return jsonify({"erro": "Token expirado"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"erro": "Token inválido"}), 401
        except Exception as e:
            return jsonify({"erro": "Erro de autenticação", "detalhe": str(e)}), 401

        return f(*args, **kwargs)

    return decorated