from flask import jsonify
from services.question_service import list_questions

def get_questions():
    data = list_questions()
    return jsonify(data), 200