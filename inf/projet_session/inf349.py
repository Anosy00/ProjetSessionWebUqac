from flask import Flask
from flask.cli import AppGroup
from app.models import db, init_db
from app.routes import bp as routes_bp
from app.services import fetch_products

def create_app():
    app = Flask(__name__)
    app.register_blueprint(routes_bp)
    return app

app = create_app()

# Commande Flask pour initialiser la base de données
@app.cli.command('init-db')
def init_db_command():
    init_db()
    fetch_products()
    print("Base de données initialisée et produits récupérés.")

if __name__ == "__main__":
    app.run(debug=True)
