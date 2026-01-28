# create_db.py
from BACKEND.Controller.app import app, db
from BACKEND.Model.User import User
from BACKEND.Model.Expense import Expense

with app.app_context():
    db.create_all()
    print("Database creato!")