from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecret'  # serve per sessioni, login ecc.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'  # il file SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # evita warning

db = SQLAlchemy(app)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(port=8000, debug=True)