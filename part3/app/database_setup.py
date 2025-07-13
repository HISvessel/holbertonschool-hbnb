"""a module for prompting separate and clean creation of databse tables"""
from app import create_app
from app.extensions.extensions import db

app = create_app()

with app.app_context():
    db.create_all()