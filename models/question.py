from models.user import db

class Question(db.Model):
    __tablename__ = "questions"

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=False)
    alternatives = db.Column(db.JSON, nullable=False)  
    correct_answer = db.Column(db.String(50), nullable=False)  
    level = db.Column(db.String(10), nullable=False)        
    content = db.Column(db.String(50), nullable=False)      
    explanation = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "question": self.question,
            "alternatives": self.alternatives,
            "correctAnswer": self.correct_answer,
            "level": self.level,
            "content": self.content,
            "explanation": self.explanation,
        }