from database.db import db
from datetime import datetime

class Category(db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False, unique=True)
    description = db.Column(db.String(500), nullable=True)
    image = db.Column(db.String(250), nullable=True)
    status = db.Column(db.String(50), default="Available", nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)   