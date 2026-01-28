from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#Colleghi SQLAlchemy all’app Flask. Così db sa con quale app e quale DB lavorare.
db = SQLAlchemy()
#Gestisce le versioni del database.
migrate = Migrate()