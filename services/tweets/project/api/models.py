# services/tweets/models.py
from sqlalchemy.sql import func

from project import db

# model
class Tweet(db.Model):
    __tablename__ = 'tweets'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128), nullable=False)
    name = db.Column(db.String(128), nullable=False)
    created = db.Column(db.DateTime, default=func.now(), nullable=False)

    def __init__(self, name, title):
        self.name = name
        self.title = title
    
    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'name': self.name,
        }
    
    