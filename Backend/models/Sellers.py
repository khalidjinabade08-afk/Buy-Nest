from database.db import db
from sqlalchemy.orm import validates
from datetime import datetime

class Seller(db.Model):
    __tablename__ = "sellers"

    id = db.Column(db.Integer, unique=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    shop_name = db.Column(db.String(250), nullable=False)
    shop_logo = db.Column(db.String(250), nullable=True)
    shop_description = db.Column(db.String(500), nullable=True)
    shop_address = db.Column(db.String(250), nullable=True)
    status = db.Column(db.String(250), default="approved")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    