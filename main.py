from flask import Flask
from db import db

def create_app():
    app = Flask(__name__, template_folder="templates")
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:password1@localhost:5432/test"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.app_context().push()
    db.init_app(app)
    db.create_all()
    return app