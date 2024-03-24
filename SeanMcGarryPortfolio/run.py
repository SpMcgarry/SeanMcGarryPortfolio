# models.py
from app import db

# Define SQLAlchemy models
class Comic(db.Model):
    __tablename__ = 'comic'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    publish_date = db.Column(db.Date)
    creator = db.Column(db.String(100))
    cover_date = db.Column(db.Date)
    drop_date = db.Column(db.Date)
    rarity = db.Column(db.Text)
    editions = db.Column(db.Integer)
    item_info = db.Column(db.Text)
    publisher = db.Column(db.Text)
    volume = db.Column(db.Integer)
    related_number = db.Column(db.Integer)
    link = db.Column(db.Text)

class Collectible(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    publish_date = db.Column(db.Date)
    creator = db.Column(db.String(100))
    drop_date = db.Column(db.Date)
    rarity = db.Column(db.Text)
    editions = db.Column(db.Integer)
    item_info = db.Column(db.Text)
    publisher = db.Column(db.Text)
    season = db.Column(db.Integer)
    related_number = db.Column(db.Integer)
    link = db.Column(db.Text)

# Define other models and relationships here
