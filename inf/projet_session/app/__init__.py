from flask import Flask
from peewee import SqliteDatabase
from app.models import init_db

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Initialisation de la base de données
    db = SqliteDatabase(app.config['SQLITE_DB'])
    init_db(db)

    # Enregistrement des routes
    from .routes import init_routes
    init_routes(app)

    return app