from flask import Flask #Importi Flask, che è il “motore” della webapp, e render_template per restituire pagine HTML con Jinja2.
from ..extensions import db, migrate #Importi SQLAlchemy, il layer ORM che ti permette di interagire con il database come se fosse Python
from ..config import Config
from ..Model import *

#Funzione factory per creare l’app Flask, cioè il server web, con tutte le sue configurazioni.
def create_app():
    #Crei l’oggetto app, cioè il server Flask vero e proprio.
    app = Flask(__name__)
    app.config.from_object(Config)

    #Inizializzi le estensioni con l’app Flask
    db.init_app(app)
    migrate.init_app(app, db)

    register_blueprints(app)

    print_routes(app)

    @app.route("/")
    def home():
        return "Backend up 🚀"

    return app

def register_blueprints(app):
    from .helloWorld import helloWorld_bp
    app.register_blueprint(helloWorld_bp)

def print_routes(app):
    for rule in app.url_map.iter_rules():
        print(rule)




#comandi utili:

#export FLASK_APP=BACKEND/Controller/app.py -> imposta la variabile d’ambiente FLASK_APP con il percorso del file principale dell’app Flask
#flask run -> avvia il server Flask
#oppure flask --app Controller.app:create_app run --port 8000 -> avvia il server Flask sulla porta 8000

#flask --app Controller.app:create_app db init -> crea la cartella migrations, da usare solo la prima volta
#flask --app Controller.app:create_app db migrate -m "messaggio" -> crea una nuova migrazione
#flask --app Controller.app:create_app db upgrade -> applica le migrazioni al database
#flask --app Controller.app:create_app db downgrade -> annulla l'ultima migrazione
#flask --app Controller.app:create_app db current -> mostra la versione corrente del database
#flask --app Controller.app:create_app db history -> mostra la cronologia delle migrazioni

#source venv/bin/activate -> attiva l’ambiente virtuale su macOS/Linux