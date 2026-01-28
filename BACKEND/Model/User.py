from ..extensions import db

class User(db.Model):
    __tablename__ = "users"

    #columns
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    isActive = db.Column(db.Boolean, default=True, nullable=False)

    #foreign relationships
    # (No foreign relationships defined here)

    #relationships
    expenses = db.relationship("Expense", backref="user", lazy=True)