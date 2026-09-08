from flask import Blueprint
from controller.user_controller import (
    register_user,
    list_users,
    login_user,
    forgot_password,
    reset_password,
     delete_user, 
)
from middleware.auth_decorator import token_required

user_bp = Blueprint("user_bp", __name__, url_prefix="/api/users")

user_bp.post("/register")(register_user)
user_bp.post("/login")(login_user)
user_bp.get("")(token_required(list_users))
user_bp.post("/forgot-password")(forgot_password)
user_bp.post("/reset-password")(reset_password)

user_bp.delete("/<int:user_id>")(token_required(delete_user))