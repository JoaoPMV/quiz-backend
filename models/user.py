from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(120), nullable=False)
    middleName = db.Column(db.String(120), nullable=True)
    lastName = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime, nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "firstName": self.firstName,
            "middleName": self.middleName,
            "lastName": self.lastName,
            "email": self.email,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }