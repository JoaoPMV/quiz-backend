from werkzeug.security import generate_password_hash, check_password_hash
from flask import current_app
import jwt
import datetime
from models.user import db, User

def create_user(firstName, middleName, lastName, email, password):
    hashed_password = generate_password_hash(password)

    user = User(
        firstName=firstName,
        middleName=middleName,
        lastName=lastName,
        email=email,
        password=hashed_password
    )

    db.session.add(user)
    db.session.commit()
    return user

def get_all_users():
    return User.query.order_by(User.id.desc()).all()

def authenticate_user(email, password):
    email = (email or "").strip().lower()
    user = User.query.filter_by(email=email).first()

    if not user:
        return None

    if not check_password_hash(user.password, password):
        return None

    token = jwt.encode(
        {
            "user_id": user.id,
            "email": user.email,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2),
        },
        current_app.config["SECRET_KEY"],
        algorithm="HS256",
    )

    return {
        "mensagem": "Login realizado com sucesso",
        "token": token
    }


def generate_reset_token(email):
    email = (email or "").strip().lower()
    user = User.query.filter_by(email=email).first()

    if not user:
        return None

    token = jwt.encode(
        {
            "user_id": user.id,
            "email": user.email,
            "type": "password_reset",
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=15),
        },
        current_app.config["SECRET_KEY"],
        algorithm="HS256",
    )

    return token

def reset_password_with_token(token, new_password):
    try:
        payload = jwt.decode(
            token,
            current_app.config["SECRET_KEY"],
            algorithms=["HS256"]
        )
    except jwt.ExpiredSignatureError:
        return {"ok": False, "erro": "Token expirado"}
    except jwt.InvalidTokenError:
        return {"ok": False, "erro": "Token inválido"}

    if payload.get("type") != "password_reset":
        return {"ok": False, "erro": "Token inválido para reset"}

    user_id = payload.get("user_id")
    user = db.session.get(User, user_id)

    if not user:
        return {"ok": False, "erro": "Usuário não encontrado"}

    user.password = generate_password_hash(new_password)
    db.session.commit()

    return {"ok": True}

def delete_user_by_id(user_id: int):
    user = db.session.get(User, user_id)
    if not user:
        return {"ok": False, "erro": "Usuário não encontrado"}

    db.session.delete(user)
    db.session.commit()
    return {"ok": True}