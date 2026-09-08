import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", "dev")
MAIL_SERVER = os.getenv("MAIL_SERVER")
MAIL_PORT = os.getenv("MAIL_PORT", 587)
MAIL_USE_TLS = os.getenv("MAIL_USE_TLS", "true")
MAIL_USERNAME = os.getenv("MAIL_USERNAME")
MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
MAIL_FROM = os.getenv("MAIL_FROM")
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:5173")

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key-123")

    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = os.getenv("MAIL_SERVER")
    MAIL_PORT = int(os.getenv("MAIL_PORT", 587))
    MAIL_USE_TLS = os.getenv("MAIL_USE_TLS", "true").lower() == "true"
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    MAIL_FROM = os.getenv("MAIL_FROM")
    FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:5173")

    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_pre_ping": True,
        "pool_recycle": 180,
        "pool_timeout": 30,
        "connect_args": {
            "sslmode": "require",
            "connect_timeout": 10,
            "application_name": "quiz-english-api"
        }
    }

    if not SQLALCHEMY_DATABASE_URI:
        raise RuntimeError("DATABASE_URL não configurada")