import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "supersecret")
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "postgresql://expenses_user:expenses_pass@localhost:5432/expenses_db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False