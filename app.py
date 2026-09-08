from flask import Flask, jsonify
from flask_cors import CORS
from models.user import db
from models.question import Question
from routes.user_routes import user_bp
from routes.question_routes import question_bp
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(question_bp)

CORS(
    app,
    resources={r"/api/*": {"origins": ["http://localhost:5173",
                                       "http://192.168.1.4:5173",]}},
    methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization"],
    supports_credentials=False,
)

db.init_app(app)
app.register_blueprint(user_bp)

@app.get("/api/health")
def health():
    return jsonify({"status": "ok"})

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)