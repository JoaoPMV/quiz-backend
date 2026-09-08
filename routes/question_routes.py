from flask import Blueprint
from controller.question_controller import get_questions

question_bp = Blueprint("question_bp", __name__)

@question_bp.get("/api/questions")
def questions():
    return get_questions()