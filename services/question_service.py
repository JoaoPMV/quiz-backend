from models.question import Question

def list_questions():
    questions = Question.query.all()
    return [q.to_dict() for q in questions]