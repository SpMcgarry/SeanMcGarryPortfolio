# __init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sigmintdata.db'
db = SQLAlchemy(app)

from app import models

# Initialize database tables within application context
with app.app_context():
    db.create_all()

# Import routes or other components of your Flask application here

