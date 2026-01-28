from ..extensions import db

class Expense(db.Model):
    __tablename__ = "expenses"

    #columns
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)

    #foreign relationships
    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    #relationships
    # (No additional relationships defined here)